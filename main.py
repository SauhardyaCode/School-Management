import mysql.connector as sql
from functions import *

try:
    con = sql.connect(host="localhost", user="root", passwd=pw.db_pswd, database="school_management")
except Exception as e:
    print("[CONNECTION ERROR]", e)
    exit()
else:
    cursor = con.cursor()

print("\n########################### Welcome To the School Management App ###########################\n")
print("\n     ########################### Login According To Your Role.. ###########################\n")
while 1:
    query = handle_q(input(roles+'\n>>> '), 4)
    if query == 1:
        while 1:
            cursor.execute("select username, password from admins")
            data = cursor.fetchall()
            key = pwinput.pwinput("\nEnter the ADMIN KEY: ")
            if key != pw.super_key:
                print("[TRY AGAIN] The ADMIN KEY you entered is incorrect!")
                break
            else:
                username = input("Enter your username: ")
                password = pwinput.pwinput("Enter your password: ")
                if (username, password) not in data:
                    print("[TRY AGAIN] Your username or password is wrong!")
                    break
                else:
                    while 1:
                        query = handle_q(input(admin_opt+'\n>>> '), 10)
                        if query == 1:
                            '''Student View'''
                            view_student(cursor)
                        elif query == 2:
                            '''Student Edit'''
                            edit_student(cursor,con)
                        elif query==3:
                            '''Student Add'''
                            add_student(cursor,con)
                        elif query == 4:
                            '''Teacher View'''
                            view_teacher(cursor,'a')
                        elif query == 5:
                            '''Teacher Edit'''
                            edit_teacher(cursor,con)
                        elif query==6:
                            '''Teacher Add'''
                            add_teacher(cursor,con)
                        elif query==7:
                            '''Password'''
                            change_pswd(cursor,con,username)
                        elif query==8:
                            '''Student Application'''
                            see_application(cursor,con,'s')
                        elif query==9:
                            '''Teacher Application'''
                            see_application(cursor,con,'t')
                        elif query:
                            step1_1 = False
                            break
                    break

    elif query == 2:
        username = input("Enter your username: ")
        pswd = pwinput.pwinput("Enter your password: ")
        cursor.execute("select username, password from teachers")
        if (username,pswd) in cursor.fetchall():
            step1_2 = True
            while step1_2:
                query = handle_q(input(teacher_opt+'\n>>> '), 5)
                if query == 1:
                    '''View Self'''
                    cursor.execute(f"select * from teachers where username='{username}'")
                    data = cursor.fetchall()
                    draw_table([x[:6] for x in data],TEACHERS[:6])
                    draw_table([x[6:] for x in data],TEACHERS[6:])
                elif query == 2:
                    '''Become Admin'''
                    become_admin(cursor,con,username)
                elif query == 3:
                    '''Student View'''
                    view_student(cursor)
                elif query == 4:
                    '''Apply Edit'''
                    apply_teacher(cursor,con,username)
                elif query:
                    step1_2 = False
        else:
            print("[TRY AGAIN] Your username or password is wrong!")
    elif query == 3:
        name = input("Enter your name: ")
        cursor.execute(f"select id,password from students where name like '%{name}%'")
        data = cursor.fetchall()
        pswd = pwinput.pwinput("Enter your student password: ")
        err = 1
        for x in data:
            if pswd==x[1]:
                err = 0
                id = x[0]
                while 1:
                    query = handle_q(input(student_opt+'\n>>> '), 5)
                    if query == 1:
                        '''View Details'''
                        cursor.execute(f"select * from students where id={id}")
                        data = cursor.fetchone()
                        draw_table([data[:6]],STUDENTS[:6])
                        draw_table([data[6:]],STUDENTS[6:])
                    elif query == 2:
                        '''Apply Edit'''
                        apply_student(cursor,con,id)
                    elif query == 3:
                        '''Teacher View'''
                        view_teacher(cursor,'s')
                    elif query:
                        break
        else:
            if err:
                print("[TRY AGAIN] Invalid name or password!")
        
    elif query:
        print("\n        ########################### Thanks For Using our App ###########################\n")
        break