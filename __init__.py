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



from flask import (Flask,render_template, redirect,
            url_for, request, make_response)

from wtforms import Form, TextField,BooleanField,PasswordField, TextAreaField, validators, StringField, SubmitField

from .routes import *

app = Flask(__name__)
app.register_blueprint(routes)

if __name__ == "__main__":
   app.run(debug= True)

