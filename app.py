import requests
import telegram
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, PicklePersistence
from bs4 import BeautifulSoup

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def fetch():
	login_url = 'https://sts.cned.fr/adfs/ls/?RelayState=X2Q4MTIxYmYyZGMzN2Y2ZmIwMzdiOTFhYjQ1ZmRlNDFiNDk5Mzc2NDc4NTAkMQ%3D%3D&SAMLRequest=tVVdb%2BI6FPwrKH2sIHYSQogaVgFaSrcUFkJXy8uVEzvEJdjUdvjor7%2BGUEp391bdla7Ei83xzHjG5%2BTqy3aZV9ZESMpZYMAaMCqEJRxTNg%2BMaXRT9YwvrSuJlrm18sNCZWxMngsiVUUfZNIv%2FwmMQjCfI0mlz9CSSF8l%2FiQc3PtWDfgrwRVPeG5UQimJUJqqw5kslkRMiFjThEzH94GRKbWSvmluNptawgi2XVBLhZkgaU4yGsc8JyqrScnNPbJljoaTSEMqJWhcKFJCat1HzD7DZKuvZFS6Wi5lSB2u%2BMoilTyw7CkQTqWZS9Oo9LuB8Y8FHOiA2HYxdlISpw6CFk6bzQbAII0dD8T12MLAhnbiOdiBTQ9CaDewZSXY0ZUJgAgjBGJUh3UQNxpN0NDQcoSkpGsSGCnKJdnvyELLlAoxFRgWsGAV6J8XQc%2B3bR%2FUa%2FWmOzMqo6N%2FbcrKXD4yOy6LpH8bRaNq6dHja766wDim6R%2FYxXmMHwOj1%2ByM1qeTujLPuVpXWPoTOtdRFIIcmbEsMznCbewaF3PTAgCYoGnqGizp%2FMI4nSW4z1J%2BWHYQ44wmKKcvh3AHmpXjSpjPuaAqW%2F4HMDQh2ANXyTapJtBhF4b5Xtongd4pFBJVZYbgEWtMUiJ0J5HKdNwPjIv%2F51EdqCKBmEy5WMr3yz%2FTT9ia5HxFcFW%2B2nC8yucBf%2B%2Bs%2BavGLp3rnvwbm88sLkEeUV6QVuYotOq43lc4%2Fe5pg93G5XXjJhs4m2lwEHBefNg4BVQuf3pap6dQnkjGjWv3xc5xNAbhFuOoByx31AvdJGnXJ%2FcOaOPLzm2PPPP1OOxtOc6d3cK15a7x4Pa6i6cfd%2FPMnd4u%2Bnfei3ywobXtbtqziVnM5pP5zfNwMIpuJzTpZBAP2eXaWckYuE%2BLWZt%2By9RscB967uMuvf7%2BdbHd9b5p3yIBL2czzK%2FvrPY2ieqh%2BSSLUWibm%2BB0nTP97%2FdO8%2FxBN3m%2FO%2BI5TXY6hpxvOoIg9TahbnRiSH08F%2FY7FFfTQ6mv9kFTwtQ%2BpLL59WDGdN%2Bf8m%2BGTeWBqzbR6OTnEWl5byNSFw3ZUISpIuKXUfpWt3%2BNv%2FmWtf4F'
	data = {
		'UserNameTemp': 'ARTYOM.BAGDASARYAN',
		'Password': 'maTVnaG2',
		'AuthMethod': 'FormsAuthentication',
		"UserName": 'edu.cned.fr\\ARTYOM.BAGDASARYAN'
	}

	with requests.Session() as s:
		response = requests.post(login_url, data)
		print(response.text)
		index_page= s.get('https://www.cned360.fr/uPortal/p/home')
		soup = BeautifulSoup(index_page.text, 'html.parser')
		print(soup)


def main():
	
	fetch()
	#pp = PicklePersistence(filename='file')
	#updater = Updater("1410913727:AAG7K8oh9ToQeZEpINTv1KfVW6Yymel_jz4", persistence=pp, use_context=True)
	#dispatcher = updater.dispatcher

	#test_handler = MessageHandler(Filters.regex('test'), test)
	#dispatcher.add_handler(test_handler)	
	

	


	#updater.start_polling()
	#updater.idle()


if __name__ == '__main__':
    main()
#for key in prices:
#	print(key.text)
