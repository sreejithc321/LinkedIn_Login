from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.conf import settings
import requests
import json
import urllib	

def code(request):
	'''Display user data from LinkedIn'''
	url = 'https://www.linkedin.com/uas/oauth2/accessToken'     
	data = {
			'client_id': settings.LINKEDIN['ID'],
			'client_secret': settings.LINKEDIN['KEY'],
			'grant_type': 'authorization_code',
			'redirect_uri' : settings.LINKEDIN['REDIRECT_URL'],
			'code': request.GET["code"]
		  }
	headers = {'Content-type': 'application/x-www-form-urlencoded'}
	r = requests.post(url, data=data, headers=headers)
	r_json = r.json()
	url = 'https://api.linkedin.com/v1/people/~:(id,first-name,last-name,maiden-name,formatted-name,phonetic-first-name,phonetic-last-name,formatted-phonetic-name,headline,location,industry,current-share,num-connections,num-connections-capped,summary,specialties,positions,picture-url,picture-urls::(original),site-standard-profile-request,api-standard-profile-request,public-profile-url,email-address)?format=json'
	headers = {'Authorization': 'Bearer {}'.format(r_json['access_token'])}
	r = requests.get(url, headers=headers)
	usr_data = r.text
	return HttpResponse(usr_data)


def linkedin(request):
	'''Redirect to LinkedIn authorization page'''
	url = 'https://www.linkedin.com/uas/oauth2/authorization?'     
	data = {
			'client_id': settings.LINKEDIN['ID'],
			'response_type': 'code',
			'redirect_uri' : settings.LINKEDIN['REDIRECT_URL'],
			'state' : 'bJkFR2mS2uVrbOxs',
			'scope' : 'r_basicprofile,rw_company_admin,r_emailaddress,w_share'
		  }
		  
	red_url = url + urllib.urlencode(data)
	#return HttpResponseRedirect('https://www.linkedin.com/uas/oauth2/authorization?response_type=code&client_id=75sas5f9w5o46m&scope=r_basicprofile%20rw_company_admin%20r_emailaddress%w_share&state=bJkFR2mS2uVrbOxs&redirect_uri=http://localhost:8080/code')
	return HttpResponseRedirect(red_url)


