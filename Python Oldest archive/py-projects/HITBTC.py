import bs4
import html5lib
import selenium;import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time as t

url='https://bitcointicker.co/'
driver = webdriver.Firefox()
driver.get(url)

for i in range(0,100):
	t.sleep(0.5)

	# try:
	heading1 = driver.find_element_by_id('lastTrade').text
	# except :
		# print('semantic error')

	print(heading1)
driver.close()





# dirs=os.sys.path
# dirs.append('/home/nikhil/Desktop/python')
# print(dirs)





# url='https://hitbtc.com/exchange/BTC-to-USDT'
# content=requests.get(url)

# soup = bs4.BeautifulSoup(content.text, 'html.parser')

# print (soup.find_all('tr'))