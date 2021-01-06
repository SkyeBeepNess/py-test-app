import requests
from bs4 import BeautifulSoup



URL = 'https://dodopizza.uz/tashkent'

page = requests.get(URL)



soup = BeautifulSoup(page.content, 'lxml')

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
a_dictionary = dict(zip_iterator)

print(dict(zip(mypizzas, myprices)))
#for key in prices:
#	print(key.text)
