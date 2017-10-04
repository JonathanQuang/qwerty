import random, hashlib
from flask import Flask, render_template, request

defaultUser = "Bob"
defaultPassword = "123" 


app=Flask(__name__)

@app.route('/')
def occu():
	if len(request.args) == 0:
		return render_template("login.html")
	else:
		if (request.args["username"]=="Bob") and (request.args["password"]=="123"):
			return render_template("loggedIn.html")

if __name__ == '__main__':
	app.debug==True
	app.run()	

	
