

# List Comprehension

**기초 활용법**

```python
a  =  [식 for 변수 in iterable if 조건문]
```



**응용**1


```python
girls = ['jane', 'iu', 'mary']
boys = ['justin', 'david', 'kim']

pair = [(x,y) for y in girls for x in boys]
```

`out`
```python
[('justin', 'jane'), ('david', 'jane'), ('kim', 'jane'), ('justin', 'iu'), ('david', 'iu'), ('kim', 'iu'), ('justin', 'mary'), ('david', 'mary'), ('kim', 'mary')]
```



**응용**2

```python
ran = range(1,51)
pita = [(x, y, z) for x in ran for y in ran for z in ran if x**2 + y**2 == z**2 and x<y<z]
```

- x y z 가 피타고라스 정리를 만족하는 50이하의 자연수쌍 구하는 코드



**응용3**

> 다음의 문장에서 모음(a, e, i, o, u)를 모두 제거하세요.

```python
words = 'Life is too short, you need python!'
```

------

```
예시 출력)
Lf s t shrt, y nd pythn!
```





In [163]:

```
new_words = [x for x in words if x not in 'aeiouAEIOU']
print(''.join(new_words))
```

`output`

```
Lf s t shrt, y nd pythn!
```





# Dictionary Comprehension

In [181]:

```
dusts = {'서울': 72, '대전': 82, '구미': 29, '광주': 45, '중국': 200}
```

In [ ]:

```
# 미세먼지 농도가 80 초과 지역만 뽑아주세요.
# 예) {'대전': 82, '중국': 200}
```

In [188]:

```
bad = {x:y for x,y in dusts.items() if y > 80}
{'대전': 82, '중국': 200}
```

In [ ]:

```
# 미세먼지 농도가 80초과는 나쁨 80이하는 보통으로 하는 value를 가지도록 바꾸세요.
```

In [199]:

```
dusts_SS = {x:'나쁨' if (y > 80) else '보통' for x,y in dusts.items()}
print(dusts_SS)
{'서울': '보통', '대전': '나쁨', '구미': '보통', '광주': '보통', '중국': '나쁨'}
```