### 1. 생성
article = Article()
article.title = '제목'
article.content = '내용'
article.save()

### 2. 조회


전체 데이터 조회
Article.objects.all()
>> <QuerySet [<Article: Article object (1)>]>


단일 데이터 조회

단일 데이터 조회는 고유한 값인 id를 통해 가능하다.

Article.objects.get(id=1)
>> <Article: Article object (1)>



### 3. 수정
a1 = Article.objects.get(id=1)
a1.title = '제목 수정'
a1.save()

수정이 되었는지  확인하기 위해서 데이터 조회를 다시 해보자.


### 4. 삭제
a1 = Article.objects.get(id=1)
a1.delete()

>> (1, {'articles.Article': 1})