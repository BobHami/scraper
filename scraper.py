'''
A websraper.

Currently this will accept a url and return all links contained on the site

http://www.pythonforbeginners.com/python-on-the-web/web-scraping-with-beautifulsoup/
'''
__author__ = 'Bob'
from bs4 import BeautifulSoup
from time import sleep #to reduce serverload

import requests

url =raw_input("Enter a website to extract the URL's from:")

r=requests.get("http://"+url)

data = r.text

soup= BeautifulSoup(data)

for link in soup.find_all('a'):
    print(link.get('href'))