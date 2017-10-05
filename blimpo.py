import random, hashlib, os
from flask import Flask, render_template, request, session

#set default user/password for testing, cause assignment never asks for a register form
defaultUser = "Bob"
defaultPassword = "123" 

#create the app and add a session/cookie
app=Flask(__name__)
app.secret_key=os.urandom(32)

@app.route('/',methods=["GET","POST"])
def occu():
	#render login page if the cookie is empty and there is no form data
	#i done goofed
	if (len(request.form) == 0) and (len(session)==0):
		return render_template("login.html")
	else:
		if (request.form["username"]=="Bob") and (request.form["password"]=="123") and len(session)==0:
			session["user"]="Bob"
			session["password"]="123"
		if (session["user"]=="Bob") and (session["password"]=="123"):
			print "cookie works"
			return render_template("loggedIn.html")

if __name__ == '__main__':
	app.debug==True
	app.run()	

	
