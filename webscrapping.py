from pprint import pprint

import bs4
import lxml
import requests


KEYWORDS = ['дизайн', 'фото', 'web', 'python']
url = 'https://habr.com/ru/articles/'
response = requests.get(url)
soup = bs4.BeautifulSoup(response.text, features='lxml')


all_articles = soup.find('div', {'class':'tm-articles-list'})
pprint(all_articles.text)