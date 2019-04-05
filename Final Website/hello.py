from flask import Flask,render_template,request,url_for,redirect,session,jsonify
from nlp import NLP
import sqlite3 as sq
import hashlib
import random




con = sq.connect('sarthak_ka_database.db')
with con:
	cur=con.cursor()
	cur.execute("Create table if not exists details(fname text not null,lname text,email text primary key not null,password text not null,weight int not null,height int not null,profession text,gender text)")


k=NLP()
app=Flask(__name__)
@app.route("/")
def index():
	return render_template('index.html')

@app.route("/login",methods =['GET','POST'])
def login():
	error =None
	if request.method == 'POST':
		username = request.form['email']
		password = request.form['password']
		password = hashlib.md5(password.encode()).hexdigest()
		con = sq.connect('sarthak_ka_database.db')
		with con:
			cur=con.cursor()
			try:
				print('checking')
				try:
					cur.execute("""SELECT fname,password  from details where email = ? """,(username,))
					d=cur.fetchone()
				except:
					print('database error')
				#print(d)
				fn = d[0]
				pas = d[1]

				print(pas,password)
				if password == pas :

					#print(username)
					return redirect(url_for('chatbot',username=fn.lower()))
				else:
					error = "Invaild Email or Password"

			except :

				error ="Email id doesn't Exist"
			print(error)
	#print(username,password)
	return render_template('login2.html',error=error)


@app.route("/signup", methods =['GET','POST'])
def signup():
	error = None
	if request.method == 'POST':
		try:
			fname = request.form['first_name']
			lname = request.form['last_name']
			bday = request.form['bday']
			email = request.form['email']
			p= request.form['password']
			ps = hashlib.md5(p.encode()).hexdigest()
			# ps = p.hexdigest()
			weight = request.form['weight']
			height = request.form['height']
			prof = request.form['profession']
			gen = request.form['gender']
			con = sq.connect('sarthak_ka_database.db')
			with con:
				try:
					cur = con.cursor()

					cur.execute("""INSERT INTO details(fname,lname,email,password,weight,height,profession,gender)VALUES(?,?,?,?,?,?,?,?)""",(fname,lname,email,ps,weight,height,prof,gen))
					print('saved')
				except:
					print('database error')
			return redirect(url_for('login'))
		except :
			error  = "Emaid id already exists"
		print(fname,lname,bday,email,ps,weight,height,prof,gen)
	return render_template('Signup.html',error =error)

@app.route("/xyz/<username>")
def chatbot(username):
	k.refresh()
	return render_template('chat.html',username = username)



@app.route('/ask', methods = ["POST"])
def ask():

	terminate_response = ['Thank you, It was nice talking to you','Thank you, see you again','Thank you, take care']
	message = request.form['messageText']
	if message.lower() == 'thank you':
		k.changeStatus(0)
		return jsonify({'status' :'OK','answer':random.choice(terminate_response)})



	if len(message):
		with open('chatting.txt','a') as f:
			f.write(message+'\n')
		k.getStatus()
		if k.getStatus() ==1:

			res = k.processing(message)[1]
			print(message)
		else:
			res = 'Personal Doctor is sleeping, Refesh the page to wake him !!'
		return jsonify({'status':'OK','answer':res})


@app.route('/logout')
def logout():
	return render_template('index.html')

if __name__=="__main__":
	app.run(port=5000,debug=True)
