from flask import render_template, request, flash
from . import routes
from flask_wtf import Form
from wtforms import TextField
from wtforms import validators, ValidationError
import pytube
import re

class YouTubeDownloaderForm(Form):
   url = TextField("Enter the video URL",[validators.Required("Please enter a URL")])



class YouTubeDownloaderCode():
	def checkYouTubeURL(self,url_str):
		try:
			yt = pytube.YouTube(url_str)
			video_streams = yt.streams.filter(file_extension='mp4').all()
			vids=[]
			for vid in video_streams:
				video_details=[round(vid.filesize/(1024*1024)),vid.url,vid.resolution]
				vids.append(video_details)

			res = ['success',yt.title,yt.thumbnail_url,vids]
		except:	
			res = ["Please enter a valid YouTube URL"]
		return res


@routes.route('/yt',methods=['POST', 'GET'])
def yt_index():
	form = YouTubeDownloaderForm()	
	result = None
	ytDloader = YouTubeDownloaderCode()
	if request.method == 'POST' and form.validate():
		url_got=request.form["url"]
		result=ytDloader.checkYouTubeURL(url_got)
		#result=checkYt_url('url_got')

	return render_template('yt_downloader.html',form=form,result=result)
#https://www.youtube.com/watch?v=EDgZLgMXb2g

