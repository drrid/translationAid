#!/usr/bin/env python
import pyperclip
import time
from requests import get
from bs4 import BeautifulSoup



#without translation
while True:
	time.sleep(1)
	clipB = pyperclip.paste()
	n_clipB = ' '.join(clipB.split())
	pyperclip.copy(n_clipB)
	print n_clipB

#
# clipB_old = ""
# while True:
# 	time.sleep(1)
# 	clipB = pyperclip.paste()
# 	if clipB_old is not clipB:
# 		clipB = ' '.join(clipB.split())
#
# 		url = get('https://translate.google.com/#en/fr/' + clipB)
# 		soup = BeautifulSoup(url.content, 'html.parser')
# 		translation = soup.find('span', id='result_box')
#
# 		pyperclip.copy(clipB)
# 		clipB_old = clipB
#
# 		print clipB
# 		print translation
