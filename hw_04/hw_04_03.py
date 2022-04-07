import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_cur(cur='USD'):
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    value = f'{cur} not found'
    report_date = datetime.strptime(soup.find('valcurs').get('date'), '%d.%m.%Y')
    for valtag in soup.find_all('valute'):
        if valtag.find('charcode').text == cur:
            value = valtag.find('value').text
    return value, f'{report_date.day} {report_date.strftime("%B")}'


print(get_cur('EUR'))
