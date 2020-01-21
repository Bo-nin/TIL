import requests
from bs4 import BeautifulSoup

market_url = "https://finance.naver.com/marketindex/"

page = requests.get(market_url).text
modi_page = BeautifulSoup(page,'html.parser')

#dollar path
#exchangeList > li.on > a.head.usd > div > span.value

dollar_ = modi_page.select_one('#exchangeList > li.on > a.head.usd > div > span.value')
#select_one (path를 str로 받음)
print(dollar_.text)

