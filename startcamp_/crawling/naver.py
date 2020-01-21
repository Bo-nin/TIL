import requests
from bs4 import BeautifulSoup

sise_url ='https://finance.naver.com/sise/'
res = requests.get(sise_url).text

soup = BeautifulSoup(res, 'html.parser')
#BeautifulSoup(문서) : 문서를 검색하기 쉽게 만들어줌(문서를 정제 str->class beautifulsoup)
#KOSPI_now
kospi = soup.select_one('#KOSPI_now')
# id가 KOSPI_now인 항목을 찾아와라 '#'은  id를 의미
print(kospi.text)

