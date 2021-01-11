import requests
import telegram
import logging
import time
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

def send(x):
	requests.post(
        url=f'https://api.telegram.org/bot1410913727:AAEBkP3V0s7pp82J7Hl15U8BMApEiU-QXBA/sendMessage?chat_id=208339045&text={x}&parse_mode=HTML'
    )
	




def testMessage(update, context):

	print(update.effective_message.chat_id)

def main():
	#today()
	
	pp = PicklePersistence(filename='file')
	updater = Updater("1410913727:AAEBkP3V0s7pp82J7Hl15U8BMApEiU-QXBA", persistence=pp, use_context=True)
	dispatcher = updater.dispatcher

	dispatcher.add_handler(MessageHandler(Filters.regex('test'), testMessage))	
	today()


	


	updater.start_polling()
	updater.idle()


if __name__ == '__main__':
    main()

#for key in prices:
#	print(key.text)
