from flask import Flask, escape, request, render_template
import random
app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'안녕하세요, {escape(name)}!'



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
@app.route('/name/<string:name>')
def val_con(name):         #url 처리하는 코드
    return render_template('name.html',html_name = name)


@app.route('/cube/<int:num>')
def cube(num):              #render_template : 미완성인 문서(cube.html)을 완성시켜주는 함수(flask 문법이다)

    return render_template('cube.html', html_num = num, cube_num = num**3)


@app.route('/lunch')
def lunch():
    menu = ['라면','닭갈비','낙지','낙지볶음밥','오므라이스']
    menu_dict = {
        '라면': 'http://t1.daumcdn.net/liveboard/realfood/3173a007147d49f6a2e32fe433cd83b1.jpg',
        '닭갈비': 'http://img.etoday.co.kr/pto_db/2019/10/20191011164701_1375452_600_362.jpg',
        '낙지': 'https://img.kbs.co.kr/kbs/620/nsimg.kbs.co.kr/data/news/2018/07/19/4011775_FdV.jpg',
        '낙지볶음밥': 'http://image.auction.co.kr/itemimage/11/7c/fa/117cfad716.jpg',
        '오므라이스': 'https://homecuisine.co.kr/files/attach/images/142/424/017/4e96c7e9fda3ede034d74d71425d4ab3.JPG',
    }
    pick = random.choice(menu)
    pick_url = menu_dict[pick]
    return render_template('lunch.html',pick = pick, pick_url = pick_url)
    

@app.route('/movies')
def movied():
    movies = ['해치치않아', '닥터두리틀', '나쁜녀석들']
    return render_template('movies.html', movies = movies)


@app.route('/ping')
def ping():
    return render_template('ping.html')

#ping 에서 받아온 데이터를 pong으로 넘겨준다 
@app.route('/pong')
def pong():
    location = request.args.get('location')
    return render_template('pong.html',location = location)

@app.route('/bon')
def bon():
    return render_template('bon.html')

@app.route('/bonbon')
def bonbon():
    dummy = request.args.get('dummy')
    companies = ['삼성','현대','LG','SK','롯데','KT','네이버','카카오','백수']
    company_dict = {
        '삼성': 'http://image.itdonga.com/files/2013/03/15/141.png',
        '현대': 'http://pr.kia.com/upload/board/content/M000000037/B000000156/F000000355.jpg',
        'LG': 'https://pbs.twimg.com/profile_images/552744521939681280/TmLhh9PT_400x400.png',
        'SK': 'http://cdn.bizwatch.co.kr/news/photo/2019/01/30/9853b71de8a1446cce2f6a9d5eb6b075.jpg',
        '롯데': 'http://www.koreaittimes.com/news/photo/201812/88132_33749_540.jpg',
        'KT': 'http://www.bloter.net/wp-content/uploads/2018/07/KT-CI_1-800x450.jpg',
        '네이버': 'https://ssl.pstatic.net/static/help/img/img_logo_naver_200X200.png',
        '카카오': 'https://t1.kakaocdn.net/kakaocorp/corp_thumbnail/Kakao.png',
        '백수': 'http://img.yonhapnews.co.kr/photo/cms/2017/10/27/05/C0A8CA3C0000015F5CB7D2A20012A69B_P2.jpeg',
    }
    pick = random.choice(companies)
    pick_img = company_dict[pick]
    return render_template('bonbon.html', pick = pick, pick_img = pick_img, dummy = dummy)

# debug mode(수정 저장 시 자동으로 서버 재시작) 하는 모드 적용코드
if __name__ == '__main__':
    app.run(debug=True)