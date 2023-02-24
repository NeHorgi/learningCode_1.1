"""
Задания:
В бою находится 3 игрока. Положение игрока на карте описывается тремя координатами
в виде списка [x, y, z]. Центр координат расположен в середине карты. X, y, z в диапазоне от -10 до 10
Необходимо:
1.	Написать функцию generate_coordinates(game_time), принимающую время,
которое игроки должны провести в игре, и возвращающую словарь вида
{время: список координат всех игроков}.
Время изменяется на 1 секунду за раз;
координаты - целые числа, генерируются случайно в разрешённом диапазоне;
игроки могут находиться в одной точке.
2.	Написать функцию extract_coordinates(coordinates),
где coordinates – сгенерированный словарь из generate_coordinates и возвращающую
плоский список неповторяющихся значений координат игроков.
Пример:
coords = generate_coordinates(0)
print(coords)
{0: [[0,1,2], [3,4,5], [6,7,8]]}
extract_coordinates(coords)
[0,1,2,3,4,5,6,7,8]
"""


import collections


def generate_coordinates(game_time):
    import random
    result = {}
    for period in range(game_time + 1):
        result[period] = [[random.randint(-10, 10) for _ in range(3)] for _ in range(3)]
    return result


def extract_coordinates(coordinates):
    result = []
    for items in coordinates[0]: # Что здесь за 0, для чего он нужен
        for item in items:
            result.append(item)
    c = collections.Counter(result)
    return sorted(list(c))


if __name__ == '__main__':
    coords = generate_coordinates(0)
    print(coords)
    print(extract_coordinates(coords))

