import requests

url = ('http://newsapi.org/v2/top-headlines?'
       'country=in&'
       'apiKey=456146a9a724410ba0b89d244c709bc1')

top_head = requests.get(url)

top_head_json = top_head.json()

# print(top_head_json)
# print(top_head_json['totalResults'])
news_head = []

def give_news():
       for i in top_head_json['articles']:
              a = i['title']
              news_head.append(a)

# print(news_head)

# for i in top_head_json['articles']:
#     print(i['title'])
