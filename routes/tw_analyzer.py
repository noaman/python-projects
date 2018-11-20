from flask import render_template,request
from . import routes
from flask_wtf import FlaskForm
from wtforms import SelectField,TextField
from wtforms import validators, ValidationError

import pickle
import os
import twitter
import json

class TwitterTrendsAnalyzerForm(FlaskForm):
    trends_country = SelectField("Enter the video URL",[validators.Required("Please enter a URL")])


class TwitterAnalyzer():
	def getTweets(self,woeid):
		Twitter={}
		Twitter['Consumer Key'] = 'eLmS48vNRMa0AJt0ZoHTPEt8K'
		Twitter['Consumer Secret'] = 'gJrUh2oe7pMdPlBNJgo5FBZbNzIXQFxbsPAHDsWnmqJK7qbjwp'
		Twitter['Access Token'] = '2376849285-1rc5bBxVZLlL3xXHjoTKi3nu4Ak9Mv3tkajedty'
		Twitter['Access Token Secret'] = 'Av75jUVxB930Coxzoj62qwp9UXAWBvOwiyhUxjXQ3aSvA'
		auth = twitter.oauth.OAuth(Twitter['Access Token'],Twitter['Access Token Secret'],Twitter['Consumer Key'],Twitter['Consumer Secret'])
		twitter_api = twitter.Twitter(auth=auth)
		WORLD_WOE_ID =woeid
		world_trends = twitter_api.trends.place(_id = WORLD_WOE_ID)
		trends_data=[]	
		for trend in world_trends[0]["trends"]:
			if(trend["tweet_volume"] is None):
				vol = 0
			else:
				vol = trend["tweet_volume"];
			if(vol>0):	
				trend_data_value=[trend["name"],trend["query"],vol,trend["url"]]
				trends_data.append(trend_data_value)

		return trends_data;



@routes.route('/tw',methods=['POST', 'GET'])
def tw_index():
	
	form = TwitterTrendsAnalyzerForm()	
	trends_woeid = 1;
	cityset=None;
	if request.method == 'POST':
		trends_woeid=request.form["country"]
		country_woeid=request.form["country"]
		cityset = request.form.get('city', None)
		if(cityset != None ):
			trends_woeid = cityset

	tweeter = TwitterAnalyzer()
	trends= tweeter.getTweets(trends_woeid)

	trends=sorted(trends, key=lambda item: item[2],reverse=True)

	return render_template('tw_analyzer.html',form=form,trends=trends,woeid_set=country_woeid,city_set=cityset)


