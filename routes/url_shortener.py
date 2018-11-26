from flask import render_template,request,redirect
import string,random
from . import routes
from flask_wtf import FlaskForm
from wtforms import TextField
from wtforms import validators, ValidationError
import os


class URL_SHORTENERFORM(FlaskForm):
    url = TextField("Enter the URL",[validators.Required("Please enter a URL")])

def string_num_generator(size):
    chars = string.ascii_lowercase + string.digits + string.ascii_uppercase
    return ''.join(random.choice(chars) for _ in range(size))
 

def createShortURl(link):
	short_url=string_num_generator(4)
	#for server side
	folderpath="/var/www/python-projects/shortlinks/"
	#for dev side local machine
	#folderpath="python-projects/shortlinks/"
	with open(folderpath+short_url, "w") as test:
		test.write(link)
		return short_url

def getLongURL(filepath):
	with open(filepath, "r") as test:
		data=test.readline()
		return data


@routes.route('/u/',methods=['POST', 'GET'])
def url_index():
	form = URL_SHORTENERFORM()	
	if request.method == 'POST' and form.validate():
		url_got=createShortURl(request.form["url"])
		path="http://py.logd.in/"+url_got
		return render_template('url_shortener.html',form=None,path=path)
	else:
		return render_template('url_shortener.html',form=form)


@routes.route('/u/<path:path>')
def url_index1(path):
	form = URL_SHORTENERFORM()
	#for server side
	#folderpath="/var/www/python-projects/shortlinks/"
	#for dev side local machine
	folderpath="python-projects/shortlinks/"
	filepath =folderpath+path
	if(os.path.isfile(filepath)):
		return redirect(getLongURL(filepath))
	else:
		return render_template('url_shortener.html',form=form)

