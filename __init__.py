#from flask import Flask

#from flask import Blueprint, render_template, abort



#app = Flask(__name__)
#@app.route("/")
#def index():
#	return render_template("index.html")


#@app.route("/yt")
#def yt_downloader():
#	return render_template("yt_downloader.html")


#if __name__ == "__main__":
#   app.run(debug= True)



from flask import (Flask,render_template, redirect,url_for, request, make_response)
from flask_wtf import Form

from wtforms import  TextField,BooleanField,PasswordField, TextAreaField, validators, StringField, SubmitField




from .routes import *

app = Flask(__name__)
app.secret_key = 'jhshs%545343543HHH**£223££##€€'
app.register_blueprint(routes)

if __name__ == "__main__":
   app.run(debug= True)

