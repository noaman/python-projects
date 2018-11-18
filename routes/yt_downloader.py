from flask import render_template
from . import routes

@routes.route('/yt',methods=['POST', 'GET'])
def yt_index():
	
	return render_template('yt_downloader.html')


