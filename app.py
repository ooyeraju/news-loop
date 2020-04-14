from flask import Flask, render_template, request
import requests
import yaml
# from news import news_head


app = Flask(__name__)
ak = yaml.load(open('ak.yaml'))

@app.route('/')
def index():
    coun_code = 'in'
    url = ('http://newsapi.org/v2/top-headlines?'
       'country={}&'
       'apiKey={}').format(coun_code, ak['api_key'])
    top_head = requests.get(url)
    top_head_json = top_head.json()
    news_head = []
    news_link = []
    news_img = []
    for i in top_head_json['articles']:
            a = i['title']
            b = i['url']
            c = i['urlToImage']
            news_head.append(a)
            news_link.append(b)
            news_img.append(c)    
    news_material = zip(news_head, news_link, news_img)
    return render_template('index.html', news_material = news_material)

@app.route('/input')
def input():
    return render_template('input.html')


@app.route('/search', methods=['POST', 'GET'])
def search():
    if request.method== 'POST':
        coun_code= request.form['coun_code']
        # print(coun_code)
        url = ('http://newsapi.org/v2/top-headlines?'
       'country={}&'
       'apiKey={}').format(coun_code, ak['api_key'])
        top_head = requests.get(url)
        top_head_json = top_head.json()
        news_head = []
        for i in top_head_json['articles']:
                a = i['title']
                news_head.append(a)
        # print(url)
        # print(news_head)
    return render_template('search.html', news_head=news_head, coun_code = coun_code )
    # return 'hi'



@app.route('/login')
def login():
    return render_template('login.html')
