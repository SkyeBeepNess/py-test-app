import requests
import telegram
import logging
import time
import webbrowser
from datetime import datetime, date
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, PicklePersistence
from bs4 import BeautifulSoup
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)




def today():
	today = date.today()
	time = datetime.now()
	# Textual month, day and year	
	d = today.strftime("%dth of %B, %Y")
	t = time.strftime("%H:%M")

	if int(t.split(':')[0]) >= 5 and int(t.split(':')[0]) < 12:
		message = "Gooooodmornin' Beepness, today is " + d + " and it's currently" + t
	elif int(t.split(':')[0]) >= 12 and int(t.split(':')[0]) < 18:
		message = "Hello Beepness, today is<code> " + d + " </code>and it's currently<code> " + t + " </code>"
		
	elif int(t.split(':')[0]) >= 18 and int(t.split(':')[0]) < 23:
		message = "Good evening Beepness, today is " + d + " and it's currently " + t
	else:
		message = "Goodnight Beepness, today is " + d + " and it's currently " + t
	send(message)

def send(message):
	requests.post(
        url=f'https://api.telegram.org/bot1560323106:AAHmhV9yoGR7i0Q4SvlJg7rAGIPyha6lZAo/sendMessage?chat_id=208339045&text={message}&parse_mode=HTML'
    )
	




def music(update, context):

	print(update.effective_message.chat_id)

	url = 'https://www.youtube.com/watch?v=Mvvsa5HAJiI&list=RDMM&start_radio=1'

	webbrowser.open_new_tab(url)

def play(update, context):
	pass
	#search = ''
	#print(update.effective_message.chat_id)
	#searchwords = update.effective_message.text.split(' ')[1:]
	#for words in searchwords:
	#	search += words + '+'
	#searchurl = 'https://www.youtube.com/results?search_query=' + search 
	#print(searchurl)
	#page = requests.get(searchurl)


	#session = HTMLSession()
	#r = asession.get("https://www.youtube.com/results?search_query=test")
	#await r.html.arender()
	#soup = BeautifulSoup(r.html.html, 'lxml')
	#print(soup)
	#url = soup.find(id="video-title")
	
	#print(url)
	#webbrowser.open_new_tab(url)


def main():
	#today()
	
	pp = PicklePersistence(filename='file')
	updater = Updater("1560323106:AAHmhV9yoGR7i0Q4SvlJg7rAGIPyha6lZAo", persistence=pp, use_context=True)
	dispatcher = updater.dispatcher

	
	dispatcher.add_handler(CommandHandler('music', music))
	dispatcher.add_handler(CommandHandler('play', play))
	today()


	#exit()


	updater.start_polling()
	updater.idle()


if __name__ == '__main__':
    main()

#for key in prices:
#	print(key.text)
