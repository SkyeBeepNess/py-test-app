import requests
import telegram
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, PicklePersistence
from bs4 import BeautifulSoup

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)



URL = 'https://dodopizza.uz/tashkent'

page = requests.get(URL)



soup = BeautifulSoup(page.content, 'lxml')
def fetch():
	mypizzas = []
	myprices = []

	pizzas = soup.find(class_="sc-814yrq-2 bVRcWG")
	titles = pizzas.find_all(class_="sc-1x0pa1d-1")
	prices = pizzas.find_all(class_="money__value")


	for pizza in titles:
		mypizzas += [pizza.text]
	for keys in prices:
		myprices += [keys.text]
	zip_iterator = zip(mypizzas, myprices)
	pp_dict = dict(zip_iterator)

	return pp_dict


def test(update, context):
	message = fetch()
	text = ''
	for keys in message:
		text += keys.strip() + ': ' + message[keys] + ' Сум \n'
	print(text)
	
	if update.effective_message.text:
		context.bot.send_message(update.effective_message.chat_id, 'Цена пицц в dodopizza.uz: \n' +  text)

def main():
	

	pp = PicklePersistence(filename='file')
	updater = Updater("1410913727:AAG7K8oh9ToQeZEpINTv1KfVW6Yymel_jz4", persistence=pp, use_context=True)
	dispatcher = updater.dispatcher

	test_handler = MessageHandler(Filters.regex('test'), test)
	dispatcher.add_handler(test_handler)	
	

	


	updater.start_polling()
	updater.idle()


if __name__ == '__main__':
    main()
#for key in prices:
#	print(key.text)
