## 기본 인자 값 (Default Argument Values)

함수가 호출될 때, 인자를 지정하지 않아도 기본 값을 설정할 수 있다.



```python
def func(p1=v1):
    return p1
```

func 함수에 인자를 넣어주지 않고 호출하더라도 설정된 기본인자로 함수가 실행된다 .



## 키워드 인자 (Keyword Arguments)

키워드 인자는 직접 변수의 이름으로 특정 인자를 전달할 수 있다.

```
def greeting(location, name='john'):
    return f'{name}은 {location}에 살고있습니다.'

```

```
greeting(name = 'hana', location = '울서')
```

`output`'hana은 울서에 살고있습니다.'



## 가변 인자 리스트 (Arbitrary Argument Lists)

앞서 설명한 `print()`처럼 개수가 정해지지 않은 임의의 인자를 받기 위해서는 가변인자를 활용합니다.

가변인자는 `tuple` 형태로 처리가 되며, 매개변수에 `*`로 표현합니다.

------

**활용법**

```python
def func(a, b, *args):
```

> `*args` : 임의의 개수의 위치인자를 받음을 의미
>
> 보통, 이 가변인자 리스트는 인자 목록의 마지막에 옵니다. (뒤의 인자들을 전부 가져가기 떄문)



```
def my_print(*args):
    print(args)
    
my_print(1,2,3,4,5)
(1, 2, 3, 4, 5)
```





## 정의되지 않은 키워드 인자들 처리하기

정의지지 않은 키워드 인자들은 `dict` 형태로 처리가 되며, `**`로 표현합니다.

주로 `kwagrs`라는 이름을 사용하며, `**kwargs`를 통해 인자를 받아 처리할 수 있습니다.



```python
def func(**kwargs):
```

> `**kwargs` : 임의의 개수의 키워드 인자를 받음을 의미



예시

```python
def my_dict(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}. ',end='')
my_dict(한국어='안녕',영어='hi')
```

