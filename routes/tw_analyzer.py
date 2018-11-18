from flask import render_template
from . import routes

@routes.route('/tw',methods=['POST', 'GET'])
def tw_index():
	return render_template('tw_analyzer.html')


