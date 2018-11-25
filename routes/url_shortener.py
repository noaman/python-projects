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
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(size))
 

def createShortURl(link):
	short_url=string_num_generator(6)
	with open("python-projects/shortlinks/"+short_url, "w") as test:
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
		return (url_got)
	else:
		return render_template('url_shortener.html',form=form)


@routes.route('/u/<path:path>')
def url_index1(path):
	filepath ="python-projects/shortlinks/"+path
	if(os.path.isfile(filepath)):
		return redirect(getLongURL(filepath))
	else:
		return ("in URL %s" %path)

