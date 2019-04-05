import sqlite3 as lite
import sys
con=lite.connect('user_signup.db')
with con:
    cur=con.cursor()
    cur.execute("Create table user_signup_table(user_fname text not null,user_lname text,user_email text primary key not null,user_password text not null,user_gender text,user_profession text,user_weight int not null,user_height int not null,user_description text)")
    cur.execute("Create table user_login_table(user_email text primary key not null,user_password not null)")
    
