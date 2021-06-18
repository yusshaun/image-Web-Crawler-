from selenium import webdriver
from bs4 import BeautifulSoup
import time
url=input("圖片網址:")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless') # 啟動無頭模式
chrome_options.add_argument('--disable-gpu')
chrome = webdriver.Chrome(chrome_options=chrome_options)
chrome.get("http://iqdb.org/")
sc = chrome.find_element_by_id("url")
sc.send_keys(url)
sc.submit()
soup = BeautifulSoup(chrome.page_source, 'html.parser')
chrome.close()
soup=soup.find_all("a", limit=2)
soup=soup[1].get('href')
if soup[0]!="h":
    soup="http:"+soup
print(soup)
