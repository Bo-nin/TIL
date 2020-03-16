##### addEventListener

```
EventTarget.addEventListener(type, listener, [, useCapture]);
```

- type : 이벤트유형
- listener : 이벤트 발생시 실행할 함수

![image-20200316112530362](C:\Users\HOME\AppData\Roaming\Typora\typora-user-images\image-20200316112530362.png)



- useCapture : 기본값 False

  기본적으로 이벤트 전파는 위에서 아래로 내려가는데 useCapture를 True로 설정한다면 이벤트전파가 위쪽으로도 향함

![image-20200316112942196](C:\Users\HOME\AppData\Roaming\Typora\typora-user-images\image-20200316112942196.png)