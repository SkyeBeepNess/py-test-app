import requests
import logging
import time
import webbrowser
from bs4 import BeautifulSoup
from requests_html import HTMLSession

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def func():
	session = HTMLSession()
	r = session.get('https://www.youtube.com/results?search_query=it%27ll+all+be+great+put+your+picture+on+my+wall+')
	r.html.render()
	soup = BeautifulSoup(r.html.html, 'lxml')
	url = soup.find('a', id="video-title")
	watch = url.get('href')
	print('===========')
	print(watch)
	print('===========')



#
#logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
#from requests_html import HTMLSession
#from bs4 import BeautifulSoup
#def func():
	#print('hello')
	#session = HTMLSession()
	#r = session.get('https://www.youtube.com/results?search_query=it%27ll+all+be+great+put+your+picture+on+my+wall+')
	#r.html.render()
	#soup = BeautifulSoup(r.html.html, 'lxml')
	#url = soup.find('a', id="video-title")
	#watch = url.get('href')
	#print('===========')
	#print(watch)
	#print('===========')