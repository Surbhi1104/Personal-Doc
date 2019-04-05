import cgitb
import sqlite3
cgitb.enable()
class db:
    try:
        conn=sqlite3.connect('user_signup.db')
        c=conn.cursor()
        def insert_values():
            print("hsd")
            form=cgi.FieldStorage()
            email=form.getvalue("email","0")
            password=form.getvalue("password","0")
            login = c.execute('SELECT * from user_signup_table WHERE email = "email" AND password = "password"')
    if (login > 0):
        print "Welcome"
    else:
        print "Login failed"
            conn.commit()
            conn.close()
    except sqlite3.Error as e:
        print(e)

c=db()
