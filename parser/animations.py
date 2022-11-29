import requests
from bs4 import BeautifulSoup as BS

URL = "https://rezka.ag/animation/"

HEADERS = {
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}


def get_html(url, params=''):
    req = requests.get(url=url, headers=HEADERS, params=params)
    return req


def get_data(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_="b-content__inline_item")
    cartoons =[]
    for item in items:
        info = item.find('div', class_='b-content__inline_item-link').find('div').string.split(', ')
        cartoon = {
            'title': item.find('div', class_='b-content__inline_item-link').find('a').string,
            'link': item.find('div', class_='b-content__inline_item-link').find('a').get('href'),
            'status': item.find('span', class_='info').string
            if item.find('span', class_='info') is not None else "Полнометражка",
        }
        try:
            cartoon['year'] = info[0]
            cartoon['country'] = info[1]
            cartoon['genre'] = info[2]
        except IndexError:
            cartoon['year'] = info[0]
            cartoon['country'] = "Unknown"
            cartoon['genre'] = info[1]

        cartoons.append(cartoon)
    return cartoons


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        animations = []
        for i in range(1, 2):
            html = get_html(f"{URL}page/{i}/")
            current_page = get_data(html.text)
            animations.extend(current_page)
        return animations

    else:
        raise Exception("Error in parser!")

