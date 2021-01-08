import requests
import telegram
import logging
import time
import mechanicalsoup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, PicklePersistence
from bs4 import BeautifulSoup
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)




def fetch_cned():
	URL = 'https://www.cned360.fr/'
	HOME = 'uPortal/p/home'
	LOGIN_ROUTE = 'https://sts.cned.fr/adfs/ls/?RelayState=X2FmOTlhY2EzNTgwN2I0NjEwNjlkYTFiNTQ3ZGNlYWU3NzM5MzEzNjUwNjAkMQ%3D%3D&SAMLRequest=tVVdb%2BI4FP0rUfpYgeMkhCRqGPE5zSxfA6EtvKyM45B0gw22A3R%2F%2FRpCKZ2ZrbojrcSLzfE5x%2Ff43tx9OaxzbUe4yBgNdFg1dI1QzOKMrgJ9FvUqrv6lcSfQOjc3frOQKZ2QbUGE1NRBKvzyn0AvOPUZEpnwKVoT4UvsT5uDvm9WDX%2FDmWSY5brWFIJwqaTajIpiTfiU8F2GyWzSD%2FRUyo3wAdjv91VMSWw5RjXhACMBpmm2XLKcyLQqBANHZhOMR9NIUUrJs2UhSUmpfJ85QxqTg7qSrnWU3Ywiebriq4qQ4qRylEBxIkAugK6FnUD%2FswaxbSe4ZifERSaE9aXlxWZiY9c1LIJj6Ng1HLsOrCfYsD1sJjXPMWqGhaCZxHDpWI6NkQKYsW0iSGqkrsoaijESItuRQE9QLshxRxTKppCIykA3DRNWDPVzI6PuQ8e3vWrN9Ra6Nj7Xr5XRMpePir0sQcK%2Fj6JxpazRw2u%2BCqCf0%2FRP6vw6xo%2BJ0Wt2euPTSd2Ba63GXSz8abZSURScnJVjUWZypttbVcZXwDQMAxgeUJhYZKsb%2FXKWxCFN2GnZRpTRDKM8%2B%2FsU7kCpslhr5ivGM5mu%2F4UYAmgciSvkgCsY2vRGB%2B%2BtfZLonUMuUEWkCJ65JiQhXHUS0WaTMNBv%2Fp9HdZKKOKIiYXwt3i%2F%2Fm39CdyRnGxJXxGsZzlf5POGvKwt%2B9tjJVqonf6fMVyUuSR5QXpAGbH2PH8H8kd2PTDIHX%2F%2BYxOsx7bYO225wMnANPm1cAiqXPzyty1MoT2yHaT9dHeY9GKazZX80pDyRbfZXN7TslwgT9iQ6960Bq08GO6uDbNuLUHRb28W8izfA6KfdyCy2YNHaIq%2Ftzrx8PDAWi3D3fBsWj4fvHtqD9ct66kDa%2BzZ0os2qWE2eHmpWyx3Nu%2Fue%2BSJusyRMn6Pu2Jy02vXxQVpfyWK3mDvu89Meev2HRTKw%2Bwcogst1rvy%2F37vM86Fq8rAzZnmGX1QMOdu3OUHybUL1VGJIfjwXjjtZXElOUF8eg84IlceQyuZXgznOjv0pfmfYaEMmW0Sxk59GJHwbkQo0oiPeTCThP%2BLMN9zxNf7iW9b4Bw%3D%3D'
	HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36', 'origin': 'https://sts.cned.fr', 'referer': 'https://sts.cned.fr/adfs/ls/?RelayState=X2FmOTlhY2EzNTgwN2I0NjEwNjlkYTFiNTQ3ZGNlYWU3NzM5MzEzNjUwNjAkMQ%3D%3D&SAMLRequest=tVVdb%2BI4FP0rUfpYgeMkhCRqGPE5zSxfA6EtvKyM45B0gw22A3R%2F%2FRpCKZ2ZrbojrcSLzfE5x%2Ff43tx9OaxzbUe4yBgNdFg1dI1QzOKMrgJ9FvUqrv6lcSfQOjc3frOQKZ2QbUGE1NRBKvzyn0AvOPUZEpnwKVoT4UvsT5uDvm9WDX%2FDmWSY5brWFIJwqaTajIpiTfiU8F2GyWzSD%2FRUyo3wAdjv91VMSWw5RjXhACMBpmm2XLKcyLQqBANHZhOMR9NIUUrJs2UhSUmpfJ85QxqTg7qSrnWU3Ywiebriq4qQ4qRylEBxIkAugK6FnUD%2FswaxbSe4ZifERSaE9aXlxWZiY9c1LIJj6Ng1HLsOrCfYsD1sJjXPMWqGhaCZxHDpWI6NkQKYsW0iSGqkrsoaijESItuRQE9QLshxRxTKppCIykA3DRNWDPVzI6PuQ8e3vWrN9Ra6Nj7Xr5XRMpePir0sQcK%2Fj6JxpazRw2u%2BCqCf0%2FRP6vw6xo%2BJ0Wt2euPTSd2Ba63GXSz8abZSURScnJVjUWZypttbVcZXwDQMAxgeUJhYZKsb%2FXKWxCFN2GnZRpTRDKM8%2B%2FsU7kCpslhr5ivGM5mu%2F4UYAmgciSvkgCsY2vRGB%2B%2BtfZLonUMuUEWkCJ65JiQhXHUS0WaTMNBv%2Fp9HdZKKOKIiYXwt3i%2F%2Fm39CdyRnGxJXxGsZzlf5POGvKwt%2B9tjJVqonf6fMVyUuSR5QXpAGbH2PH8H8kd2PTDIHX%2F%2BYxOsx7bYO225wMnANPm1cAiqXPzyty1MoT2yHaT9dHeY9GKazZX80pDyRbfZXN7TslwgT9iQ6960Bq08GO6uDbNuLUHRb28W8izfA6KfdyCy2YNHaIq%2Ftzrx8PDAWi3D3fBsWj4fvHtqD9ct66kDa%2BzZ0os2qWE2eHmpWyx3Nu%2Fue%2BSJusyRMn6Pu2Jy02vXxQVpfyWK3mDvu89Meev2HRTKw%2Bwcogst1rvy%2F37vM86Fq8rAzZnmGX1QMOdu3OUHybUL1VGJIfjwXjjtZXElOUF8eg84IlceQyuZXgznOjv0pfmfYaEMmW0Sxk59GJHwbkQo0oiPeTCThP%2BLMN9zxNf7iW9b4Bw%3D%3D'}

	

	s = requests.session()
	
#	#csrf_token = s.get(URL).cookies['csrf']

	login_payload = {
		'UserNameTemp': 'ARTYOM.BAGDASARYAN',
		'Password': 'maTVnaG2',
		'AuthMethod': 'FormsAuthentication',
		"UserName": "edu.cned.fr\\ARTYOM.BAGDASARYAN"
	}

	#login_req = s.post(LOGIN_ROUTE, headers=HEADERS, data = login_payload)
	login_req = requests.get(LOGIN_ROUTE, auth=(login_payload["UserNameTemp"], login_payload["Password"]))
	print(login_req)
	cookies = login_req.cookies
	page = requests.get(URL + HOME)
	print(page)
	soup = BeautifulSoup(s.get(URL+HOME).text, 'lxml')

	print(soup)
	print(fetch_cned)

#	schedule = soup.find(class_="schedule")
	
#	titles = pizzas.find_all(class_="sc-1x0pa1d-1")
#	prices = pizzas.find_all(class_="money__value")

	
	#print(soup)




def testMessage(update, context):
	pass

def main():
	fetch_cned()
	
	#pp = PicklePersistence(filename='file')
	#updater = Updater("1410913727:AAG7K8oh9ToQeZEpINTv1KfVW6Yymel_jz4", persistence=pp, use_context=True)
	#dispatcher = updater.dispatcher

	#test_handler = MessageHandler(Filters.regex('test'), testMessage)
	#dispatcher.add_handler(test_handler)	


	


	#updater.start_polling()
	#updater.idle()


if __name__ == '__main__':
    main()

#for key in prices:
#	print(key.text)
