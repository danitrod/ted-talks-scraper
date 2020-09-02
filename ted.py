import json
from urllib import request

from bs4 import BeautifulSoup as BS


def main(url):
    page = request.urlopen(url)
    soup = BS(page, 'html.parser')

    author_title = str(
        soup.find('title').get_text()).split('|')[0]
    [author, title] = author_title.split(':')

    body = str(soup.find('div', attrs={'class': 'p:2'}).get_text()).replace(
        '\t', '').replace('(Risos)', '').replace('(Aplausos)', '').replace('(Vivas)', '').replace('\n', ' ')

    obj = {
        "author": author.strip(),
        "body": body.strip(),
        "title": title.strip(),
        "type": "video",
        "url": url
    }

    file_name = '_'.join(title.replace('.', '').strip().split(' ')) + '.json'
    with open(file_name, 'w', encoding='utf8') as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)

    return obj
