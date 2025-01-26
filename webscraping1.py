import requests
import pandas
from bs4 import BeautifulSoup
url = 'https://www.bankbazaar.com/reviews.html'

HEADERS = ({'User-Agent':
			'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
			AppleWebKit/537.36 (KHTML, like Gecko) \
			Chrome/90.0.4430.212 Safari/537.36',
			'Accept-Language': 'en-US, en;q=0.5'})


def getdata(url):
	r = requests.get(url, headers=HEADERS)
	return r.text


def html_code(url):
	htmldata = getdata(url)
	soup = BeautifulSoup(htmldata, 'html.parser')

	return (soup)

soup = html_code(url)
print(soup)


def cus_data(soup):
	data_str = ""
	cus_list = []

	for item in soup.find_all("span", class_="review-bank-title"):
		data_str = data_str + item.get_text()
		cus_list.append(data_str)
		data_str = ""
	return cus_list


cus_res = cus_data(soup)
print(cus_res)
