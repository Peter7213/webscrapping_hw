from pprint import pprint

import bs4
import lxml
import requests


KEYWORDS = ['дизайн', 'фото', 'web', 'python']
url = 'https://habr.com/ru/articles/'
headers = {'User-Agent': 'Crome'}
response = requests.get(url, headers=headers, timeout=10)
response.raise_for_status()                                         #Для проверки положительного ответа
soup = bs4.BeautifulSoup(response.text, features='lxml')

all_articles = soup.select('article')
for article_data in all_articles:
    title_tag = article_data.select_one('a.tm-title__link')
    new_url = 'https://habr.com' + title_tag.get('href')

    response_mk2 = requests.get(new_url, headers=headers, timeout=10)
    response_mk2.raise_for_status()
    soup_2 = bs4.BeautifulSoup(response_mk2.text, features='lxml')

    article = soup_2.select_one('article')
    article_body = article.select('div')
    article_text = ' '.join(block.get_text(' ', strip=True) for block in article_body)

    time_tag = article.select_one('[datetime]')

    title = title_tag.get_text('span', strip=True)
    date_time_ = time_tag.get('datetime', '')[:10]

    if any(keyword.lower() in article_text for keyword in KEYWORDS):
        print(f'{date_time_} - {title} - {new_url}')

    if __name__ == '__main__':
        pass

