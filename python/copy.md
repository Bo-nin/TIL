# COPY

- list , dictionary등은 복사를 할때 value가 아니라 value의 주소를 복사함으로 값 변경이 용이하지 않다.
- 이럴때 이용할 수 있는게 copy
- 만일 중첩된 상황에서 복사를 하고 싶다면, `깊은 복사(deep copy)`를 해야한다.
- 즉, 내부에 있는 모든 객체까지 새롭게 값이 변경된다.

 ##### 깊은 복사

```
import copy

a = [1,2,3]
b = copy.copy(a)

a = [[1,2], [3,4], [5,6]]
b = copy.deepcopy(a)
```

