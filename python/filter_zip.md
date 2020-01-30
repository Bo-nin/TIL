## `zip(*iterables)`

- 복수의 iterable 객체를 모아준다.

- 결과는 튜플의 모음으로 구성된 `zip object` 를 반환한다.

In [14]:

```python
girls = ['jane', 'iu', 'mary']
boys = ['justin', 'david', 'kim']
```

In [15]:

```python
list(zip(girls, boys))
```

Out[15]:

```python
[('jane', 'justin'), ('iu', 'david'), ('mary', 'kim')]
```





예제

```python
# 한 명씩 순서대로 매칭시켜봅시다.
# 예) {'jane': 'justin', 'iu': 'david', 'mary': 'kim'}
```



```python
new_dict = {x:y for x in girls for y in boys }
new_dict #dict의 경우 알아서 잘 분류된다 개쩐다
```

`output`

```python
{'jane': 'kim', 'iu': 'kim', 'mary': 'kim'}
```



```python
dict(zip(girls, boys))

```

`output`

```python
{'jane': 'justin', 'iu': 'david', 'mary': 'kim'}
```



In [28]:

```python
num1= '123'
num2= '456'
for a,b in zip(num1, num2):
    print (a,b)
```

```python
1 4
2 5
3 6
```





## `filter(function, iterable)`

- iterable에서 function의 반환된 결과가 `True` 인 것들만 구성하여 반환한다.

- `filter object` 를 반환한다.

### 홀수인지 판단하는 코드

```
def hol(num):
    if num%2 == 1:
        return True
    else :
        return False
a = [1,2,3,4,5]
b = list(filter(hol,a))
b
```

```
[1, 3, 5]
```