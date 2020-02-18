# 모듈

다른 python파일을 import하여 자유롭게 사용 가능

```python
# import를 이용하여 fibo.py를 가져옵니다.
import fibo
```





```
fibo.fibo_recursion(10)
```

```
55
```



##### 모듈의 이름 변경

```python
from myPackage.web import url as my_url
print(my_url)
```



##### 모듈 사용법

```python
import module
import pakage1.module1, pakage2.module2
from module import var
from module import function
from module import Class
from module import *
from pakage.module import var, function, Class
```

##### 패키지 사용법

- jupyter notebook 파일트리화면에서 New > Folder
- 다음과 같은 폴더구조 생성

```python
myPackage/
    __init__.py
    math/
        __init__.py
        formula.py
    web/
        __init__.py
        url.py
```





### math

|                함수 |                            비고 |
| ------------------: | ------------------------------: |
|        math.ceil(x) |                     소수점 올림 |
|       math.floor(x) |                     소수점 내림 |
|       math.trunc(x) |                     소수점 버림 |
| math.copysign(x, y) |        y의 부호를 x에 적용한 값 |
|        math.fabs(x) | float 절대값 - 복소수 오류 발생 |
|   math.factorial(x) |                팩토리얼 계산 값 |
|     math.fmod(x, y) |               float 나머지 계산 |
| math.fsum(iterable) |                        float 합 |
|        math.modf(x) |              소수부 정수부 분리 |





### random

```python
import random

lotto = random.sample(range(1, 46), 6)

random.shuffle(my_list)

random.random()

random.seed ... 
```





### datetime

```
import datetime
now = datetime.now()

```

- 시간 형식지정

| 형식 지시자(directive) |                   의미 |
| ---------------------: | ---------------------: |
|                     %y |        연도표기(00~99) |
|                     %Y |         연도표기(전체) |
|                     %b |          월 이름(축약) |
|                     %B |          월 이름(전체) |
|                     %m |         월 숫자(01~12) |
|                     %d |              일(01~31) |
|                     %H |     24시간 기준(00~23) |
|                     %I |     12시간 기준(01~12) |
|                     %M |              분(00~59) |
|                     %S |              초(00~61) |
|                     %p |              오전/오후 |
|                     %a |             요일(축약) |
|                     %A |             요일(전체) |
|                     %w | 요일(숫자 : 일요일(0)) |
|                     %j |  1월 1일부터 누적 날짜 |



| 속성/메소드 |                 내용 |
| ----------: | -------------------: |
|       .year |                   년 |
|      .month |                   월 |
|        .day |                   일 |
|       .hour |                   시 |
|     .minute |                   분 |
|     .second |                   초 |
|  .weekday() | 월요일을 0부터 6까지 |

##### timedelta

```python
from datetime import timedelta

christmas = datetime.datetime(2020, 12, 25)
now = datetime.datetime.today()
christmas - now
while True:
    print(christmas - now)
```

