### DOM

- window
  - 전역객체, 해당 창이 가진 모든 요소를 가진다
- document
  - html 문서와 연결된 키워드



##### DOM 접근

![image-20200316111346845](C:\Users\HOME\AppData\Roaming\Typora\typora-user-images\image-20200316111346845.png)

```javascript
document.querySelector(selector)
document.querySelectorA;;(selector)
//위의 두가지 선택자를 중심으로 사용하는게 좋다.
```



##### DOM 조작

```javascript
element.insertAdjacentHTML(position, text)
//문서 안에 직접 텍스트를 추가할 수있는 구문
```

