from dataclasses import dataclass
from bs4 import BeautifulSoup
import requests


def get_a_format_table():

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


@dataclass
class CompanyInfo:
    name: str
    popularity: int
    front: str
    back: str
    database: str
    notes: str


def make_a_data_table():

    company_info = []
    data_name = 'info'
    result = get_a_format_table()

    for _ in range(len(result)):
        data_name += result[_][0]
        company_info.append(data_name)
        data_name = 'info'

    for _ in range(len(company_info)):
        company_info[_] = CompanyInfo(
            result[_][0],
            result[_][1],
            result[_][2],
            result[_][3],
            result[_][4],
            result[_][5]
        )

    return company_info


if __name__ == '__main__':
    get_a_format_table()
    for _ in make_a_data_table():
        print(_.name, '|', _.popularity, '|', _.front, '|', _.back)
