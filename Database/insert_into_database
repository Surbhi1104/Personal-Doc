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
            fname=form.getvalue("first_name","0")
            lname=form.getvalue("last_name","0")
            gender=form.getvalue("gender","0")
            email=form.getvalue("email","0")
            password=form.getvalue("password","0")
            dob=form.getvalue("bday","0")
            profession=form.getvalue("profession","0")
            c.execute("insert into user_sign_up_table(user_fname,user_lname,user_gender,user_email,user_password,user_dob,user_profession,user_weight,user_height,user_description) values (fname,lname,gender,email,password,dob,profession)")
            conn.commit()
            conn.close()
    except sqlite3.Error as e:
        print(e)

c=db()
