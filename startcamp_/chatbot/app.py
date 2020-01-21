from flask import Flask, escape, request, render_template
import requests
import random
from bs4 import BeautifulSoup
app = Flask(__name__)



token = '1042735388:AAHAMxAPzNv7EG7rG6crWSbV44myebd0ET0'
url = f'https://api.telegram.org/bot{token}/'
my_id = 844110452
ngrok_url = 'https://40bcb124.ngrok.io' #ngrok으로 만든 임시url
papago_api_id = 'YKTz2BEbhAoXzg6RRaYC'
papago_api_secret = 'uXxIqqny_Q'


@app.route('/')
def hello():
    webhook = f'{url}setWebhook?url={ngrok_url}/telegram'
    return webhook

@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/send')
def send():
    msg = request.args.get('msg')
    # 텔레그램 url에 sendmessage 메서드 사용 , 넘기는 변수로 chat_id와 text
    msg_url = f'{url}sendmessage?chat_id={my_id}&text={msg}'
    res = requests.get(msg_url)
    print(res.text)
    return render_template('send.html',msg = msg)

#webhook

@app.route('/telegram', methods=['POST'])
def telegram():
    res = request.get_json()
    user_id = res['message']['from']['id']
    user_msg = res['message']['text']
    # print(user_id , user_msg)
    trans = user_msg.split('/')

    #사용자의 메시지{user_msg}에 따른 분기처리
    if user_msg == '안녕' :
        return_msg = '반가워요'

    elif user_msg == '점심메뉴' :
        menu = ['중식', '한식', '일식', '양식']
        return_msg = random.choice(menu)

    elif user_msg == '로또':        #로또번호 긁어오기
        lotto_url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%EB%A1%9C%EB%98%90'
        lotto_num_page = requests.get(lotto_url).text
        lotto_num_modi = BeautifulSoup(lotto_num_page, 'html.parser')
        lotto_num = lotto_num_modi.select_one('#_lotto > div.lotto_wrap > div.num_box')
        return_msg = lotto_num.text[0:-10]

    #elif user_msg[0:2] == '번역':
    elif trans[0] == '번역':
        before = trans[2]
        headers = {
            'X-Naver-Client-Id': papago_api_id,
            'X-Naver-Client-Secret':papago_api_secret,
        }
        papago_url = 'https://openapi.naver.com/v1/papago/n2mt'
        
        data = {
            'source': 'ko',
            #'target': 'en',
            'text': before,
        }
        data['target'] = trans[1]

        res = requests.post(papago_url, headers=headers, data=data)
        after = res.json()['message']['result']['translatedText']
        #after = res.json().get('message').get('result').get('trenslatedText')
        return_msg = after

    else:
        return_msg = '지원하지 않는 명령어입니다.'




    send_url = f'{url}sendMessage?chat_id={user_id}&text={return_msg}'
    requests.get(send_url)
    return '',200



if __name__ == '__main__':
    app.run(debug=True)