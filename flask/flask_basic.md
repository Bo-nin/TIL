# 2020-01-16

### flask를 이용한 웹구축 기초

##### html 문서의 문법 기초

```html
    <form action="/bonbon">
        이름을 적어주세요 : <input name = "dummy">
        <input type="submit">
    </form>
```

- form 안의 action으로 제출 후  action 옆에 걸린 "/bonbon"으로 이동
- input은 유저에게 데이터를 입력받는 기능

- type = "submit"은 제출버튼

```html
    {% if pick == '백수'%}
    <h1>{{dummy}}님은 안타깝게도 영원히 {{pick}}입니다 ㅠㅠ</h1>
    <img src="{{pick_img}}">
    {% else %}
    <h1>{{dummy}}님은 향후에 {{pick}} 에서 일하게 됩니다!</h1>
    <img src="{{pick_img}}">
    {% endif %}
```

- 파이썬에서 건네 받은 변수는 {{여기 안에}} 넣으세요
- 조건 혹은 반복문은 {% 여기 %} 안에 넣고 끝날때는 {% endif %}를 넣어요



##### flask를 사용한 웹구축 (flask = web framework)

```python
from flask import Flask, escape, request, render_template
import random
app = Flask(__name__)
```

- 라이브러리 참조

시작때 set FLASK_APP = "hello.py"

```python
@app.route('/welcome')  #라우팅 처리(요청에 따른 path 설정)
def welcome():
    return '반갑습니다.'
                        #사용자의 요청에 따른 응답

@app.route('/html_tag')
def html_tag():
    return '<h1>헤딩 1번입니다</h1>'

@app.route('/first')    #미리 만들어둔 html 반환
def first():
    return render_template('hello.html')

#변수라우팅 코드
@app.route('/name/<string:name>') 	#여러가지 주소를 한꺼번에 처리
def val_con(name):         			#url 처리하는 코드
    return render_template('name.html',html_name = name)


@app.route('/cube/<int:num>')
def cube(num):              #render_template : 미완성인 문서(cube.html)을 완성시켜주는 함수(flask 문법이다)

    return render_template('cube.html', html_num = num, cube_num = num**3)
```



```python
@app.route('/bon')
def bon():
    return render_template('bon.html')

@app.route('/bonbon')
def bonbon():
    dummy = request.args.get('dummy')
    companies = ['삼성']
    company_dict = {
        '삼성': 'http://image.itdonga.com/files/2013/03/15/141.png',
	}
    pick = random.choice(companies)
    pick_img = company_dict[pick]
    return render_template('bonbon.html', pick = pick, pick_img = pick_img, dummy = dummy)
```

- bon.html에서 이름을 입력받아 bonbon.html에다 랜덤한 값을 뽑아 보내는 페이지구축





```python
# debug mode(수정 저장 시 자동으로 서버 재시작) 하는 모드 적용코드
if __name__ == '__main__':
    app.run(debug=True)
```

실행시에는 cmd창에서 'python hello.py' 를 입력하여 실행하였음