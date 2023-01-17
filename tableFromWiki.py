from dataclasses import dataclass, field, fields
from typing import List, Any


from bs4 import BeautifulSoup
import requests


url = requests.get('https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites')
soup = BeautifulSoup(url.text, "html.parser")
wiki_table = soup.table


result = []


def getAFormatTable():

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


if __name__ == '__main__':
    print(getAFormatTable())
