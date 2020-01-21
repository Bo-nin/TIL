# github 관리

git bash를 이용



### 명령어

```bash
git init
```

현재 directory를 git으로 관리하겠다 선언하는 느낌

.git이라는 숨김파일을 생성한다



```bash
git remote add origin https://github.yourname.reponame.git
```

url 경로를 origin이라는 이름으로 저장하고 그를 git의 remote서버로 설정



```bash
git add .
```

새로 생성된 파일을 git 관리 안에 넣는 명령어\

add 뒤에 `.`은 해당 git 폴더 전체를 뜻하며 path를 넣어 개별지정도 가능



```bash
git commit -m "message"
```

```bash
git push -u origin master
```

`origin url`에 `master`  브랜치로 remote 저장



```bash
git diff
```

이전 버전과 현재 로컬이 어떻게 다른지 알수있는 명령어

```bash
git status
git log
```

`status`는 git 전체상태, `log`는 커밋 로그를 보여준다



```
git pull
```

`pull`을 통해서 서버의 데이터로 최신화를 시킨 후에 코딩하자