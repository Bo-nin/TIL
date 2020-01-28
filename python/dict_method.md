# 딕셔너리 메소드 활용

## 추가 및 삭제

### `.pop(key[, default])`

key가 딕셔너리에 있으면 제거하고 그 값을 돌려줍니다. 그렇지 않으면 default를 반환합니다.

default가 없는 상태에서 딕셔너리에 없으면 KeyError가 발생합니다.

```
# pop을 사용해봅시다.
my_dict = {'apple': '사과', 'banana': '바나나'}
```

```python
my_dict.pop('apple')
print(my_dict)
{'banana': '바나나'}
```

In [168]:

```python
my_dict.pop('melon')
print(my_dict)
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-168-407060bba2b2> in <module>
----> 1 my_dict.pop('melon')
      2 print(my_dict)

KeyError: 'melon'
```

`# 두번째 인자로 default를 설정할 수 있습니다.`

In [170]:

```
my_dict.pop('melon', '해당 키는 없습니다') 
#pop () 에서 해당 키가 없을경우 두번째 인자 반환
```

Out[170]:

```
'해당 키는 없습니다'
```



### .update()`

값을 제공하는 key, value로 덮어씁니다.

In [171]:

```
# update를 사용해봅시다.
my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}
```

In [174]:

```python
my_dict.update(orange ='어린쥐이이이')
print(my_dict)
{'apple': '사과아아아아', 'banana': '바나나', 'melon': '멜론', 'orange': '어린쥐이이이'}
```

### `.get(key[, default])`

key를 통해 value를 가져옵니다.

절대로 KeyError가 발생하지 않습니다. default는 기본적으로 None입니다.

In [175]:

```python
# get을 사용해봅시다.
my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}
my_dict['pineapple']
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-175-d3cdd6ee6d26> in <module>
      1 # get을 사용해봅시다.
      2 my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}
----> 3 my_dict['pineapple']

KeyError: 'pineapple'
```

In [178]:

~~~python
my_dict.get('pineapple')
## Dictionary comprehension

dictionary도 comprehension을 활용하여 만들 수 있습니다. 

---

**활용법**

```python
{키: 값 for 키, 값 in 딕셔너리}

dict({키: 값 for 키, 값 in 딕셔너리})

{키: 값 for 키, 값 in 딕셔너리 if 조건식}

{키: 값 if 조건식 else 값 for 키, 값 in 딕셔너리}

```
~~~

In [ ]:

```
# dictionary comprehension
```

In [180]:

```python
a = [1,2,3]
cubic_dict = {x : x**2 for x in a}
print(cubic_dict)
{1: 1, 2: 4, 3: 9}
```



### Dictionary comprehension 사용해보기

In [181]:

```
dusts = {'서울': 72, '대전': 82, '구미': 29, '광주': 45, '중국': 200}
```



##### 미세먼지 농도가 80 초과 지역만 뽑아주세요.

In [188]:

```python
bad = {x:y for x,y in dusts.items() if y > 80}
print(bad)
{'대전': 82, '중국': 200}
```



##### 미세먼지 농도가 80초과는 나쁨 80이하는 보통으로 하는 value를 가지도록 바꾸세요.

In [199]:

```python
dusts_SS = {x:'나쁨' if (y > 80) else '보통' for x,y in dusts.items()}
print(dusts_SS)
{'서울': '보통', '대전': '나쁨', '구미': '보통', '광주': '보통', '중국': '나쁨'}
```