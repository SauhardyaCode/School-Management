from constants import *
import passwords as pw
import pwinput
import re

# to draw the sql table
def draw_table(data, table):
    data.insert(0, table)
    col = [[] for _ in range(len(data[0]))]
    for i in range(len(data[0])):
        for j in range(len(data)):
            col[i].append(data[j][i])
    high = []
    for x in col:
        big = 0
        for i in range(len(x)):
            if len(str(x[i]))>len(str(x[big])):
                big=i
        high.append(len(str(x[big])))

    def breaker():
        print('\n+',end='')
        for h in high:
            print('-'*(h+2), end='+')

    breaker()
    print('\n|', end='')
    for i,x in enumerate(table):
        print(' '+x+' '*(high[i]-len(x)+1), end='|')
    breaker()
    for i,x in enumerate(data[1:]):
        print('\n|', end='')
        for j,y in enumerate(x):
            try:
                print(' '+y+' '*(high[j]-len(y)+1), end='|')
            except:
                print(' '*(high[j]-len(str(y))+1)+str(y)+' ', end='|')
    breaker()
    print('\n')

# to handle a user input
def handle_q(query, sno):
    try:
        query = int(query)
        1/query
    except:
        opt = [f'{i}+' if i==sno else i for i in range(1,sno+1)]
        print("Choose among [",end='');print(*opt,sep=', ',end='');print("]")
    else:
        return query

# to view student details (teacher+admin)
def view_student(cursor):
    while 1:
        query = handle_q(input(s_det_opt+'\n>>> '), 5)
        if query == 1:
            cursor.execute("select id,name,class,roll,address,father,mother,sex,email,phone from students")
            draw_table(cursor.fetchall(), STUDENTS[:-1])
        elif query == 2:
            clas = input("Enter class whose record you want to see: ")
            cursor.execute(f"select id,name,class,roll,address,father,mother,sex,email,phone from students where class like '{clas}%'")
            draw_table(cursor.fetchall(), STUDENTS[:-1])
        elif query == 3:
            address = input("Enter address of student whose record you want to see: ")
            cursor.execute(f"select id,name,class,roll,address,father,mother,sex,email,phone from students where address like '{address}%'")
            draw_table(cursor.fetchall(), STUDENTS[:-1])
        elif query == 4:
            while 1:
                query = handle_q(input(s_info_opt+'\n>>> '), 4)
                if query == 1:
                    try:
                        id = int(input("Enter Database ID of student: "))
                    except:
                        print("[TYPE ERROR] ID must be an integer!")
                    else:
                        cursor.execute(f"select * from students where id={id}")
                        data = cursor.fetchall()
                        if data:
                            draw_table(data, STUDENTS)
                        else:
                            print("[TRACKING FAILURE] No student identified with this ID!")
                elif query == 2:
                    try:
                        roll = int(input("Enter class Roll Number of student: "))
                    except:
                        print("[TYPE ERROR] Roll Number must be an integer!")
                    else:
                        cursor.execute(f"select id,name,class,roll,address,father,mother,sex,email,phone from students where roll={roll}")
                        data = cursor.fetchall()
                        if data:
                            draw_table(data, STUDENTS[:-1])
                        else:
                            print("[TRACKING FAILURE] No student identified with this Roll Number!")
                elif query == 3:
                    name = input("Enter Name or part of Name of student: ")
                    cursor.execute(f"select id,name,class,roll,address,father,mother,sex,email,phone from students where name like '%{name}%'")
                    data = cursor.fetchall()
                    if data:
                        draw_table(data, STUDENTS[:-1])
                    else:
                        print("[TRACKING FAILURE] No student identified with this name!")
                elif query:
                    break
        elif query:
            break

# to edit student details (admin)
def edit_student(cursor,con):
    try:
        id = int(input("Enter Database ID of student: "))
    except:
        print("[TYPE ERROR] ID must be an integer!")
    else:
        cursor.execute(f"select id,name,class,roll,address,father,mother,sex,email,phone from students where id={id}")
        data = cursor.fetchall()
        if data:
            print(f"\nHere is the details of student with ID {id}")
            draw_table(data, STUDENTS[:-1])
            while 1:
                query = handle_q(input(s_edit_opt+'\n>>> '), 10)
                if query == 3:
                    try:
                        updated = int(input("Enter the updated information: "))
                    except:
                        print(f"[TYPE ERROR] {STUDENTS[3]} must be an integer!")
                    else:
                        if input("Are you sure to change it (y/n)? ").lower().startswith('y'):
                            cursor.execute(f"update students set {STUDENTS[query]}={updated} where id={id}")
                elif query and query<10 and query>0:
                    updated = input("Enter the updated information: ")
                    if input("Are you sure to change it (y/n)? ").lower().startswith('y'):
                        cursor.execute(f"update students set {STUDENTS[query]}='{updated}' where id={id}")
                elif query:
                    con.commit()
                    print("[SUCCESS] Saved Changes Successfully!")
                    break
        else:
            print("[TRACKING FAILURE] No student identified with this ID!")

# to add a student (admin)
def add_student(cursor,con):
    while 1:
        print("Start entering the details of the student\n")
        name = input("Name: ")
        while 1:
            clas = input("Class: ")
            if re.match(r"(?:(?:0|)[1-9]|1[0-2])[A-Z]",clas):
                break
            else:
                print("[TYPE ERROR] Class must be of the format 10A, 11B, 9C, etc..!")
        while 1:
            try:
                roll = int(input("Roll: "))
                break
            except:
                print("[TYPE ERROR] Roll must be an integer!")
        address = input("Address: ")
        father = input("Father: ")
        mother = input("Mother: ")
        while 1:
            sex = input("Sex (M/F): ").lower()
            if sex.startswith('m') or sex.startswith('f'):
                sex=sex[0].upper()
                break
            else:
                print("[DATA ERROR] M or F !!\n")
        while 1:
            email = input("Email: ")
            if re.match(r"[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",email):
                break
            else:
                print("[DATA ERROR] Invalid Email ID!")
        while 1:
            phone = input("Phone: ")
            if re.match(r"\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d+",phone):
                break
            else:
                print("[DATA ERROR] Invalid phone number!")
        while 1:
            pswd = pwinput.pwinput("Create Student Password (minimum 6 characters): ")
            confirm = pwinput.pwinput("Confirm Password: ")
            if len(pswd)<6:
                print("[DATA ERROR] Password doesn't match criteria!")
            if pswd!=confirm:
                print("[DATA ERROR] Confirmed password doesn't match created password!")
            else:
                break

        if input("Do you want to add this record (y/n)? ").lower().startswith('y'):
            cursor.execute(f"insert into students(name,class,roll,address,father,mother,sex,email,phone,password)\
            values('{name}','{clas}',{roll},'{address}','{father}','{mother}','{sex}','{email}','{phone}','{pswd}')")
            con.commit()
            print("[SUCCESS] Student Added Successfully!")
            break

# to view teacher details (admin+student)
def view_teacher(cursor, role):
    while 1:
        query = handle_q(input(t_det_opt+'\n>>> '), 5)
        if role=='a':
            details = "id,name,address,degree,sex,email,phone,subjects,salary,admin"
        else:
            details = "name,address,degree,sex,subjects"
        if query == 1:
            cursor.execute(f"select {details} from teachers")
            draw_table(cursor.fetchall(), details.split(','))
        elif query == 2:
            subject = input("Enter a subject that the teacher teaches: ")
            cursor.execute(f"select {details} from teachers where subjects like '%{subject}, %' or subjects like '%, {subject}%'")
            draw_table(cursor.fetchall(), details.split(','))
        elif query == 3:
            address = input("Enter the address of the teacher: ")
            cursor.execute(f"select {details} from teachers where address like '%{address}%'")
            draw_table(cursor.fetchall(), details.split(','))
        elif query==4:
            while 1:
                query = handle_q(input(t_info_opt+'\n>>> '), 3)
                if query == 1:
                    try:
                        id = int(input("Enter Database ID of teacher: "))
                    except:
                        print("[TYPE ERROR] ID must be an integer!")
                    else:
                        cursor.execute(f"select {details} from teachers where id={id}")
                        data = cursor.fetchall()
                        if data:
                            draw_table(data, details.split(','))
                        else:
                            print("[TRACKING FAILURE] No teacher identified with this ID!")
                elif query == 2:
                    name = input("Enter Name or part of Name of teacher: ")
                    cursor.execute(f"select {details} from teachers where name like '%{name}%'")
                    data = cursor.fetchall()
                    if data:
                        draw_table(data, details.split(','))
                    else:
                        print("[TRACKING FAILURE] No teacher identified with this name!")
                elif query:
                    break
        elif query:
            break

# to edit teacher details (admin)
def edit_teacher(cursor,con):
    try:
        id = int(input("Enter Database ID of teacher: "))
    except:
        print("[TYPE ERROR] ID must be an integer!")
    else:
        cursor.execute(f"select id,name,address,degree,sex,email,phone,subjects,salary,admin,username from teachers where id={id}")
        data = cursor.fetchall()
        if data:
            print(f"\nHere is the details of teacher with ID {id}")
            draw_table(data, TEACHERS)
            while 1:
                query = handle_q(input(t_edit_opt+'\n>>> '), 9)
                if query == 8:
                    try:
                        updated = int(input("Enter the updated information: "))
                    except:
                        print(f"[TYPE ERROR] {TEACHERS[8]} must be an integer!")
                    else:
                        if input("Are you sure to change it (y/n)? ").lower().startswith('y'):
                            cursor.execute(f"update teachers set {TEACHERS[query]}={updated} where id={id}")
                elif query and query<8 and query>0:
                    updated = input("Enter the updated information: ")
                    if input("Are you sure to change it (y/n)? ").lower().startswith('y'):
                        cursor.execute(f"update teachers set {TEACHERS[query]}='{updated}' where id={id}")
                elif query:
                    con.commit()
                    print("[SUCCESS] Saved Changes Successfully!")
                    break
        else:
            print("[TRACKING FAILURE] No student identified with this ID!")

# to add a teacher (admin)
def add_teacher(cursor,con):
    while 1:
        print("Start entering the details of the teacher\n")
        name = input("Name: ")
        address = input("Address: ")
        degree = input("Degree: ")
        while 1:
            sex = input("Sex (M/F): ").lower()
            if sex.startswith('m') or sex.startswith('f'):
                sex=sex[0].upper()
                break
            else:
                print("[DATA ERROR] M or F !!\n")
        while 1:
            email = input("Email: ")
            if re.match(r"[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",email):
                break
            else:
                print("[DATA ERROR] Invalid Email ID!")
        while 1:
            phone = input("Phone: ")
            if re.match(r"\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d+",phone):
                break
            else:
                print("[DATA ERROR] Invalid phone number!")
        subjects = input("Subjects: ")
        while 1:
            try:
                salary = int(input("Salary: "))
                break
            except:
                print("[TYPE ERROR] Salary must be an integer!")
        cursor.execute("select username from teachers")
        users = cursor.fetchall()
        while 1:
            username = input("Username: ")
            if (username,) in users:
                print("[TRY AGAIN] Username already taken!")
            else:
                break
        while 1:
            pswd = pwinput.pwinput("Create Password (minimum 6 characters): ")
            confirm = pwinput.pwinput("Confirm Password: ")
            if len(pswd)<6:
                print("[DATA ERROR] Password doesn't match criteria!")
            if pswd!=confirm:
                print("[DATA ERROR] Confirmed password doesn't match created password!")
            else:
                break
        if input("Do you want to add this record (y/n)? ").lower().startswith('y'):
            cursor.execute(f"insert into teachers(name,address,degree,sex,email,phone,subjects,salary,admin,username,password)\
            values('{name}','{address}','{degree}','{sex}','{email}','{phone}','{subjects}',{salary},'NO','{username}','{pswd}')")
            con.commit()
            print("[SUCCESS] Teacher Added Successfully!")
            break

# to change local password (admin)
def change_pswd(cursor,con,username):
    admin = pwinput.pwinput("Enter the ADMIN KEY: ")
    if admin==pw.super_key:
        old = pwinput.pwinput("Enter your current password: ")
        cursor.execute("select username, password from admins")
        if (username,old) in cursor.fetchall():
            while True:
                new = pwinput.pwinput("Enter your new password (minimum 6 characters): ")
                if len(new)>6:
                    confirm = pwinput.pwinput("Confirm your new password: ")
                    if new==confirm:
                        cursor.execute(f"update admins set password='{new}' where username='{username}'")
                        con.commit()
                        print("[SUCCESS] Password updated succesfully!")
                        break
                    else:
                        print("[DATA ERROR] Your password doesn't match confirmation password!\n")
                else:
                    print("[DATA ERROR] Your password doesn't match the criteria!\n")
                repeat = input("Do you want to exit (y/n)? ").lower()
                if repeat.startswith('y'):
                    break
        else:
            print("[TRY AGAIN] Your current password is wrong!")
    else:
        print("[TRY AGAIN] Wrong ADMIN KEY!")

# to become an admin (teacher)
def become_admin(cursor,con,username):
    cursor.execute(f"select admin from teachers where username='{username}'")
    already = cursor.fetchone()[0]
    if already=='YES':
        print("[NEWS] You are already an admin!")
    else:
        admin = pwinput.pwinput("Enter the ADMIN KEY to become an admin: ")
        if admin==pw.super_key:
            while 1:
                pswd = pwinput.pwinput("Create your admin login password (at least 6 characters): ")
                if len(pswd)<6:
                    print("[DATA ERROR] Password doesn't match criteria!")
                    continue
                confirm = pwinput.pwinput("Confirm your password: ")
                if pswd!=confirm:
                    print("[DATA ERROR] Confirmed password doesn't match created password!")
                else:
                    cursor.execute(f"select email,phone from teachers where username='{username}'")
                    email,phone = cursor.fetchone()
                    cursor.execute(f"update teachers set admin='YES' where username='{username}'")
                    cursor.execute(f"insert into admins(username,password,email,phone)\
                    values ('{username}','{pswd}','{email}','{phone}')")
                    con.commit()
                    print("[SUCCESS] You have become an admin now!")
                    break
        else:
            print("[TRY AGAIN] Wrong Admin Key!")

# to apply for changes (student)
def apply_student(cursor,con,id):
    change = ['name','address','email','phone']
    while 1:
        query=handle_q(input("What do you want to change?"+s_apply_opt+"Apply Changes (Back)\n>>> "),5)
        if query and query<5 and query>0:
            cursor.execute(f"select {change[query-1]} from students where id={id}")
            old = cursor.fetchone()[0]
            updated = input("Enter the updated information: ")
            if input("Are you sure to apply for this change (y/n)? ").lower().startswith('y'):
                cursor.execute(f"insert into app_student(student_id,category,old,new)\
                values('{id}','{change[query-1]}','{old}','{updated}')")
        elif query:
            con.commit()
            print("[SUCCESS] Applied for Changes Successfully!")
            break

# to apply for changes (teacher)
def apply_teacher(cursor,con,username):
    change = ['name','address','degree','email','phone']
    while 1:
        query=handle_q(input("What do you want to change?"+t_apply_opt+"Apply Changes (Back)\n>>> "),6)
        if query and query<5 and query>0:
            cursor.execute(f"select {change[query-1]} from teachers where username='{username}'")
            old = cursor.fetchone()[0]
            updated = input("Enter the updated information: ")
            if input("Are you sure to apply for this change (y/n)? ").lower().startswith('y'):
                cursor.execute(f"insert into app_teacher(username,category,old,new)\
                values('{username}','{change[query-1]}','{old}','{updated}')")
        elif query:
            con.commit()
            print("[SUCCESS] Applied for Changes Successfully!")
            break

# to view and approve applications (admin)
def see_application(cursor,con,role):
    if role=='s':
        change = ['name','address','email','phone']
        table = "app_student"
        table_base = "students"
        heading = APPS
        option = s_apply_opt
        condition = "id= "
    else:
        change = ['name','address','degree','email','phone']
        table = "app_teacher"
        table_base = "teachers"
        heading = APPT
        option = t_apply_opt
        condition = "username=''"

    while 1:
        query=handle_q(input(apply_view_opt+'\n>>> '),3)
        if query==1:
            cursor.execute(f"select * from {table}")
            draw_table(cursor.fetchall(),heading)
        elif query==2:
            while 1:
                query=handle_q(input("Choose category"+option+"Nothing (Back)\n>>> "),len(change))
                if query and query>0 and query<=len(change):
                    cursor.execute(f"select * from {table} where category='{change[query-1]}'")
                    draw_table(cursor.fetchall(),heading)
                elif query:
                    break
        elif query==3:
            while 1:
                try:
                    id = int(input("Enter the application ID to be approved: "))
                except:
                    print("[TYPE ERROR] Application ID must be an integer!")
                else:
                    break
            cursor.execute(f"select * from {table} where id={id}")
            data = cursor.fetchone()
            if data:
                print(f"\nThis is the application with ID {id}")
                draw_table([data],APPS)
                confirm = input("Are you sure you want to approve this (y/n)? ").lower()
                if confirm.startswith('y'):
                    cursor.execute(f"update {table_base} set {data[2]}='{data[4]}' where {condition[:-1]}{data[1]}{condition[-1]}")
                    cursor.execute(f"delete from {table} where id={data[0]}")
                    con.commit()
                    print(f"[SUCCESS] Application ID {id} approved successfully!")
            else:
                print("[TRACKING FAILURE] No Application identified with this ID!")
        elif query:
            break