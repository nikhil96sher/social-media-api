import api
from django.shortcuts import render,get_object_or_404,render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect,Http404,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from urllib2 import urlopen,Request,HTTPError
import simplejson as json
import urllib
import base64
# Create your views here.
class tweet():
	def __init__(self,user,graphic,text,time):
		self.user = user
		self.graphic = graphic
		self.text = graphic
		self.time = graphic

def findstory(request):
	hashtag=request.GET.get('tag',"twitter")
	token.getbearertoken()
	bearer_token = token.returnbearertoken()
	
	#Use facebook and twitter api to get result
	twitter_url="https://api.twitter.com/1.1/search/tweets.json?q=%23"+hashtag;
	raw=urllib.urlopen(twitter_url)
	js=raw.readlines()
	js_object=json.loads(js[0])
	tweets=[]
	print js_object
	'''
	for item in js_object['results']:
		user = item['from_user']
		graphic = item['profile_image_url']
		text = item['text']
		time = item['created_at']
		thistweet=tweet(user,graphic,text,time)
		tweets.append(thistweet)
	'''
	return render(request,'hashtag/result.html',{'tweets':js_object})

def home(request):
	token.getbearertoken();
	return render(request,'hashtag/home.html',)

class token():
	bearer_token=""
	
	@staticmethod
	def getbearertoken():
		API_Key = api.api_key
		API_Secret = api.api_secret
		token = API_Key+':'+API_Secret
		encoded_token = base64.b64encode(token.encode('ascii'))
		auth_url = "https://api.twitter.com/oauth2/token"
		req = Request(auth_url)
		req.method="POST"
		req.add_header('Content-Type','application/x-www-form-urlencoded;charset=UTF-8')
		req.add_header('Authorization','Basic %s' % token.decode('utf-8'))
		data = 'grant_type=client_credentials'.encode('ascii')
		response = urlopen(req,data)
		raw_data = response.read().decode('UTF-8')
		data = json.loads(raw_data)
		bearer_token = data['access_token']

	@staticmethod
	def returnbearertoken():
		if(token.bearer_token==""):
			token.getbearertoken()
		return token.bearer_token