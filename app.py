from flask import Flask, render_template
import requests
# from news import news_head


app = Flask(__name__)

@app.route('/')
def index():
    coun_code = 'in'
    url = ('http://newsapi.org/v2/top-headlines?'
       'country={}&'
       'apiKey=456146a9a724410ba0b89d244c709bc1').format(coun_code)
    top_head = requests.get(url)
    top_head_json = top_head.json()

    news_head = []
    for i in top_head_json['articles']:
            a = i['title']
            news_head.append(a)

    return render_template('index.html', news_head = news_head)

@app.route('/login')
def login():
    return render_template('login.html')
