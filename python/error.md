# Exceptions

### try / except

```python
try:
    codeblock1
except 예외(에러명):
    codeblock2
```



`예제`

```python
num = input('숫자를 넣어주세요')
try:
    print(100/int(num))
# except Exception:
#     print('뭔가 잘못된것같아')
except ZeroDivisionError:
    print('0으로는 나눌 수 없어')
except ValueError:
    print('숫자를 넣어달라고')
finally:
    print('이건 그냥 출력')
```



## 예외 발생시키기

```python
raise

raise IndexError('에러설명')
```

