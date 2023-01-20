import pytest
import requests
from bs4 import BeautifulSoup

nums = [10 ** 7, 1.5 * 10 ** 7, 5 * 10 ** 7, 10 ** 8, 5 * 10 ** 8, 10 ** 9, 1.5 * 10 ** 9]


@pytest.fixture
def take_a_table():

    url = requests.get('https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites')
    soup = BeautifulSoup(url.text, "html.parser")
    wiki_table = soup.table

    result = []

    for num in wiki_table.find_all('tr'):
        string = []
        for mun in num.find_all('td'):
            while True:
                if mun.select_one('sup'):
                    mun.select_one('sup', class_='reference').decompose()
                else:
                    break
            string.append(mun.get_text(strip=True))
        if string:
            result.append(string)

    for number in result:
        num = number[1].split(' ')
        num = num[0].replace(',', '')
        num = num.replace('.', '')
        number[1] = int(num)

    return result


@pytest.mark.parametrize('num', nums)
def test_1(num, take_a_table):

    error = []

    for _ in take_a_table:

        if num > _[1]:
            error.append(_)

    assert not error, [f'{row[0]} (Frontend:{row[2]}|Backend:{row[3]}) has {row[1]} unique visitors per month. (Expected less than {num})' for row in error]
