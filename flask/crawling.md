### 크롤링

- requests 라이브러리

- bs4 > BeautifulSoup 라이브러리

```python
import requests
from bs4 import BeautifulSoup
```

- 라이브러리 호출


```python
market_url = "https://finance.naver.com/marketindex/"

page = requests.get(market_url).text
modi_page = BeautifulSoup(page,'html.parser')
```

- url을 requests.get 으로 따와 text정보만 저장

- 이를 BeautifulSoup에 넣어 정제과정을 거친다 (두번째 인자는 정제할 문서의 형식)



```python
dollar_ = modi_page.select_one('#exchangeList > li.on > a.head.usd > div > span.value')
print(dollar_.text)
```

- #select_one (path를 str로 받음)

- 정제가 끝난 modi_page에(class : BeautifulSoup 로 바뀐 상태) select_one 함수로 정보를 정확하게 가져옴

- 가져온 정보의 text만 출력



