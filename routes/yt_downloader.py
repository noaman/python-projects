from flask import render_template
from . import routes
from flask_wtf import Form
from wtforms import TextField

class YouTubeDownloaderForm(Form):
   name = TextField("URL")


@routes.route('/yt',methods=['POST', 'GET'])
def yt_index():
	form = YouTubeDownloaderForm()	
	return render_template('yt_downloader.html',form=form)


