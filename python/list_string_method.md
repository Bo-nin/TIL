# 문자열 메소드 활용하기

## 변형

### `.capitalize()`, `.title()`, `.upper()`

- `.capitalize()` : 앞글자를 대문자로 만들어 반환한다.
- `.title()` : 어포스트로피나 공백 이후를 대문자로 만들어 반환한다.
- `.upper()` : 모두 대문자로 만들어 반환한다.

```
a = 'hI! Everyone, I\'m kim'

# 아래에 코드를 작성하세요.
```

```
print(a.capitalize())
print(a.title())
print(a.upper())

Hi! everyone, i'm kim
Hi! Everyone, I'M Kim
HI! EVERYONE, I'M KIM
```







### `.replace(old, new[, count])`

바꿀 대상 글자를 새로운 글자로 바꿔서 반환합니다.

count를 지정하면 해당 갯수만큼만 시행합니다.

```
'hello!!!'.replace('llo','110110'[0:3])
```

```
'he110!!!'
```





```
a = 'apple'
a.replace('p','*',1)
```

```
'a*ple'
```



### `.strip([chars])`

특정한 문자들을 지정하면, 양쪽을 제거하거나 왼쪽을 제거하거나(lstrip), 오른쪽을 제거합니다(rstrip).

지정하지 않으면 공백을 제거합니다.



```
a = input('데이터를 입력해주세요 : ')
print(a.rstrip())
데이터를 입력해주세요 :    123   
   123
```

```
print('       123         '.lstrip())
print('       123         '.rstrip())
123         
       123
```



In [54]:

```
'hihihihihihihihihihihehe'.strip('hi')
```

Out[54]:

```
'ehe'
```



## 탐색 및 검증

### `.find(x,[start, end])`

x의 첫 번째 위치를 반환합니다. 없으면, -1을 반환합니다.

In [67]:

```
a = 'abbbabbbabbbabbb'
print(a.find('a', 5 , 7))
print(a.find('a', 5 , 9))
-1
8
```