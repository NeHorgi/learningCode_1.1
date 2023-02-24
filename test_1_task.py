import requests
import tableFromWiki
import pytest
from dataclasses import dataclass
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
    # TODO поработать над неймингом переменных и функций!!!

    #TODO Запихнуть сюда формирование листа с датаклассами и уже их подавать в качеста параметров для теста
    #FIXME ADASD
    return result


@pytest.mark.parametrize('num', nums)
def test_1(num, take_a_table):

    error = []

    for _ in take_a_table:
    #TODO поправить нейминг используеммых переменных
        if num > _[1]:
            error.append(_)

    assert not error, '\n'.join([f'{row[0]} (Frontend:{row[2]}|Backend:{row[3]}) has {row[1]} unique visitors per month. (Expected less than {num})' for row in error])


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
    result = take_a_table()

    for _ in range(len(result)):
        data_name += result[_][0]
        company_info.append(data_name)
        data_name = 'info'

    # TODO избавиться от создания списка с именами для датаклассов, и сразу перейти к созданию датаклассов
    # TODO избавить от индексации
    # TODO обращаться сразу к элементам списка, а не итерироваться по индексам

    #for info in company_info:


    for _ in range(len(company_info)):
        company_info[_] = CompanyInfo(*result[_])
        company_info[_] = CompanyInfo(
            result[_][0],
            result[_][1],
            result[_][2],
            result[_][3],
            result[_][4],
            result[_][5]
        )

    return company_info

'''
if __name__ == '__main__':
    take_a_num()
    for _ in make_a_data_table():
        print(_.name, '|', _.popularity, '|', _.front, '|', _.back)
'''
