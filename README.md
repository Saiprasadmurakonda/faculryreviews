# facultyreviews
Download and install Xampp, now start apache and my sql in xampp. 
If there is an error in starting sql, it means your system has MYSQL downloaded already, so go to taskbar manager and search for sql, mysqld will be there, right click and end that task
Now go to localhost, it should display contents of xampp
Copy paste the code in vscode editor, in cmd of vscode, enter "pip install pymysql"
Now you are all set, go to localhost/phpmyadmin
Create a database sms2, with tablename data2
Create a table with the columns:rollno,name,class_var,section,syllabus,interest,quiz,punctual,opinion
Now save changes in database. Go to vscode cmd, enter python facultyreviews.py
