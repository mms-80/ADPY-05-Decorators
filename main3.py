import os
import bs4
import requests
from utils import _logger


@_logger('Logs/3.log')
def web_scrap():
    path = '3.log'
    if os.path.exists(path):
        os.remove(path)

    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'accept': '*/*'
        }

    words = {'web', 'python', 'Настройка'}

    url_habr = 'https://habr.com/ru/all/'
    response = requests.get(url_habr, headers=HEADERS)
    text = response.text

    soup = bs4.BeautifulSoup(text, features="html.parser")
    articles = soup.find_all(class_="tm-article-snippet tm-article-snippet")

    for article in articles:
        post = article.find('h2', class_="tm-article-snippet__title tm-article-snippet__title_h2")
        a_post = set(post.text.split())
        hubs = article.find(class_="tm-article-snippet__hubs")
        a_hubs = set(hubs.text.split())

        if words & (a_post | a_hubs):
            date = article.find('time').text
            title = article.find('h2').find('a').find('span').text
            post_h = article.find('a')
            href = post_h.attrs['href']
            url = 'https://habr.com' + href
            print(f'Дата: {date} - Заголовок: {title}   Ссылка: {url}')

            result = f'Дата: {date}\n - Заголовок: {title}\n   Ссылка: {url}'
            return result


if __name__ == '__main__':
    web_scrap()