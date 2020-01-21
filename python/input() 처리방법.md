# input() 처리방법

##### 알고리즘 문제등에서 input이 무기한 반복되는 경우에 적용하는법

```python
while True :
    try :
        input() #문제에 따라 입력값을 컨트롤 하세요
    except :
        break
```

input 직접 입력시 입력값이 끝나면 현재 프로세스 종료 후 엔터