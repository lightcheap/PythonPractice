
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
url = 'https://disclosure.edinet-fsa.go.jp/E01EW/BLMainController.jsp?uji.verb=W1E63031Search&uji.bean=ee.bean.W1E63030.EEW1E63031Bean&PID=W1E63030&TID=W1E63031&SESSIONKEY=1505008790454&stype=0&dcdSelect=12001&hcdSelect=01001&ycdSelect=03001400&tsbSdt=&kbn=1&lgKbn=2&pkbn=0&skbn=1&dskb=&askb=&dflg=0&iflg=0&preId=1&chr=%E6%B2%BF%E9%9D%A9&hbn=true&spf5=2&otd=12001&hcd=01001&ycd=03001400&sec=&scc=&snm=&spf1=1&spf2=1&iec=&icc=&inm=&spf3=1&fdc=&fnm=&spf4=1&cal=1&era=H&yer=&mon=&psr=1&pid=4'
browser = webdriver.Chrome("C:/chromedriver_win32/chromedriver")
browser.implicitly_wait(10)
browser.get(url)
assert 'EDINET' in browser.title
links = browser.find_element_by_css_selector('.table_border_1 > a')
company_name = links[1].text
links[1].click()