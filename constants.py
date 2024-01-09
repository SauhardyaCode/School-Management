#constants
STUDENTS = ('id', 'name', 'class', 'roll', 'address', 'father', 'mother', 'sex', 'email', 'phone', 'password')
TEACHERS = ('id', 'name', 'address', 'degree', 'sex', 'email', 'phone', 'subjects', 'salary', 'admin', 'username', 'password')
APPS = ('id', 'student_id', 'category', 'old', 'new')
APPT = ('id', 'username', 'category', 'old', 'new')

#options
roles = '''\n\t\t(1) Admin Login
\t\t(2) Teacher Login
\t\t(3) Student Login
\t\t(4) Exit'''
admin_opt = '''\n\t\t(1) View Students Info
\t\t(2) Edit Students Info
\t\t(3) Add New Student
\t\t(4) View Teachers Info
\t\t(5) Edit Teachers Info
\t\t(6) Add New Teacher
\t\t(7) Change Your Password
\t\t(8) View Student Applications
\t\t(9) View Teacher Applications
\t\t(10) Back'''
teacher_opt = '''\n\t\t(1) View Your Details
\t\t(2) Become Admin
\t\t(3) Get Student Details
\t\t(4) Apply To Change Details
\t\t(5) Back'''
student_opt = '''\n\t\t(1) View Your Details
\t\t(2) Apply To Change Details
\t\t(3) Know Your Teachers
\t\t(4) Back'''
s_det_opt = '''\n\t\t(1) View Full Record
\t\t(2) View Class-wise Record
\t\t(3) View Address-wise Record
\t\t(4) View Record of a particular student
\t\t(5) Back'''
s_info_opt = '''\nWhat do know about the student?
\t\t(1) Database ID
\t\t(2) Roll Number
\t\t(3) Name
\t\t(4) Nothing (Back)'''
s_edit_opt = '''\nWhat do you want to change?
\t\t(1) Name
\t\t(2) Class
\t\t(3) Roll Number
\t\t(4) Address
\t\t(5) Father's name
\t\t(6) Mother's name
\t\t(7) Sex
\t\t(8) Email ID
\t\t(9) Phone No.
\t\t(10) Save Changes (Back)'''
t_det_opt = '''\n\t\t(1) View Full Record
\t\t(2) View Subject-wise Record
\t\t(3) View Address-wise Record
\t\t(4) View Record of a particular teacher
\t\t(5) Back'''
t_info_opt = '''\nWhat do know about the teacher?
\t\t(1) Database ID
\t\t(2) Name
\t\t(3) Nothing (Back)'''
t_edit_opt = '''\nWhat do you want to change?
\t\t(1) Name
\t\t(2) Address
\t\t(3) Degree
\t\t(4) Sex
\t\t(5) Email ID
\t\t(6) Phone No.
\t\t(7) Subjects
\t\t(8) Salary
\t\t(9) Save Changes (Back)'''
s_apply_opt = '''\n\t\t(1) Name
\t\t(2) Address
\t\t(3) Email ID
\t\t(4) Phone No.
\t\t(5) '''
apply_view_opt = '''\n\t\t(1) View all applications
\t\t(2) View applications by category
\t\t(3) Approve application
\t\t(4) Back'''
t_apply_opt = '''\n\t\t(1) Name
\t\t(2) Address
\t\t(3) Degree
\t\t(4) Email ID
\t\t(5) Phone No.
\t\t(6) '''