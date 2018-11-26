from flask import render_template,request
from . import routes
from flask_wtf import FlaskForm
from wtforms import SelectField,TextField
from wtforms import validators, ValidationError

import pickle
import os
import twitter
import json
import pandas as pd
import operator
from pprint import pformat


#class TwitterHashtagsAnalyzer:
def getHashTagTweets(q,num=100):
	#local machine file path
	#filepath = "python-projects/passwords/twitter_creds.passwords"
	
	#q = '#modi'
	#server file path
	filepath = "/var/www/python-projects/passwords/twitter_creds.passwords"

	Twitter = {}
	with open("python-projects/passwords/twitter_creds.passwords", "r") as file:
		Twitter['Consumer Key'] = file.readline().strip()
		Twitter['Consumer Secret'] = file.readline().strip()
		Twitter['Access Token'] = file.readline().strip()
		Twitter['Access Token Secret'] = file.readline().strip()

	auth = twitter.oauth.OAuth(Twitter['Access Token'],Twitter['Access Token Secret'],Twitter['Consumer Key'],Twitter['Consumer Secret'])
	twitter_api = twitter.Twitter(auth=auth)
	search_results = twitter_api.search.tweets(q=q,count=100,result_type='recent')

	search_results1 = twitter_api.search.tweets(q=q,count=100,result_type='popular')

	all_text=[]
	filtered_status=[]
	for s in search_results["statuses"]:
	     if not s["text"] in all_text:
	            filtered_status.append(s)
	            all_text.append(s["text"])
	for s in search_results1["statuses"]:
	     if not s["text"] in all_text:
	            filtered_status.append(s)
	            all_text.append(s["text"])
	                        

	statuses=filtered_status

	
	tweet_results = []
	for result in statuses:
		post_type='text'
		media_url='na'
		video_duration="na"
		video_link="na"
		rt_count = result["retweet_count"]
		fv_count= result["favorite_count"]
		hashtags=result['entities']['hashtags']

		if(result.get('extended_entities') != None):
			post_type=result['extended_entities']['media'][0]['type']
			media_url =result['extended_entities']['media'][0]['media_url']
			video_duration="na"
			video_link="na"
			
			

			if(result['extended_entities']['media'][0].get('video_info') !=  None):
				if(result['extended_entities']['media'][0]['video_info']['duration_millis']!= None):
					video_duration=result['extended_entities']['media'][0]['video_info']['duration_millis']
				video_link=result['extended_entities']['media'][0]['video_info']['variants'][0]['url']
		
			if(result.get('retweeted_status') != None):
				hashtags=result['retweeted_status']['entities']['hashtags']
				rt_count=result['retweeted_status']['retweet_count']
				fv_count=result['retweeted_status']['favorite_count']
			

		resultarray = {'user':result['user']["name"],
						'screen_name':result['user']["screen_name"],
						'profile_image_url':result['user']["profile_image_url"],
						'retweet_count':rt_count,
						'favorite_count':fv_count,
						'description':result['user']["description"],
						'followers_count':result['user']["followers_count"],
						'verified':result['user']["verified"],
						'created_at':result['created_at'],
						'text':result['text'],
						'truncated':result['truncated'],
						'type':post_type,
						'media_url':media_url,
						'video_duration':video_duration,
						'video_link':video_link,
						'hashtags':hashtags
						#'possibly_sensitive':result['user']['possibly_sensitive']
						}
		tweet_results.append(resultarray) 

	
	#tweet_results=sorted(tweet_results, key=lambda item: item[2],reverse=True)	
	return tweet_results

		

class TwitterHashtagsAnalyzerForm(FlaskForm):
    hashtag_text = TextField("Enter the Hash tag",[validators.Required("Please enter a Hashtag")])


@routes.route('/twhash',methods=['POST','GET'])
def twhash_index():
	form = TwitterHashtagsAnalyzerForm()
	hashtag=None
	#twitter_analyzer = TwitterHashtagsAnalyzer()
	if request.method == 'POST':
		hashtag = "#"+request.form.get('hashtag').strip()
		twitter_response = getHashTagTweets(hashtag)
		return render_template('tw_hashtag_list.html',form=form,hashtag=hashtag,response=twitter_response)
	else:	
		return render_template('tw_hashtag_list.html',form=form,hashtag=hashtag)
