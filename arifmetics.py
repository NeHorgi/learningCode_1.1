"""
Задания:
Напишите функцию get_sum(value), принимающую любое значение, и возвращающую
сумму его чисел, если это возможно, и None ,если невозможно.
Пример:
get_sum(123)
6
(т.е. 1+2+3)
"""


def get_sum(value):

    result = 0

    if type(value) == int: #isinstance - глянуть почему лучше
        while value > 0:
            digit = value % 10
            result += digit
            value = value // 10
        return result

    if type(value) == float:
        value = str(value)
        value = value.replace('.', '')
        value = list(value)
        value = map(int, value)
        result = sum(value)
        return result
    if type(value) == dict:
        for k,v in value.items():
            try:
                int(v)
                result += int(v)
            except:
                continue

    if type(value) == bool or value == None:
        return None
    for num in value:
        try:
            int(num)
            result += int(num)
        except:
            continue

    if result == 0:
        return None
    # TODO обработка сценария, когда в ходе работы функции мы получаем result == 0

    return result


"""
3. Есть функция:
"""

def add_gold(value):
    if value > 1_000:
        raise RuntimeError('Cannot add so much:( Please mercy!')
    print(f'{value} of gold added:) I am breathtaking!')

"""
Невозможно начислить больше 1000 золота за раз.
Напишите функцию add_some_gold(value), принимающую любое значение, и начислите 
требуемое количество золота используя функцию add_gold.
"""


def add_some_gold(value): #Лучше не изменять параметры, получаемые на вход
    result = 0
    flag = False
    while not flag: # Или пока переменная не будет меньше нуля
        try:
            add_gold(value)
            result += value
            flag = True
        except RuntimeError:
            add_gold(999)
            result += 999
            value -= 999 #Можно и 1000
    div, mod = divmod(value, 1000)
    [add_gold(1000) for _ in range(div)]
    add_gold(mod)
    return result

    # TODO как решить, если не известно ограничение по начислению, оптимизация эдишн!


if __name__ == '__main__':
    print(get_sum(123))
    print(get_sum(2.124))
    print(get_sum('123'))
    print(get_sum('abs124fds'))
    print(get_sum([1,2,3]))
    print(get_sum({'a': 1, 'b': 4}))
    print(get_sum({1, 2, 'f', 4}))
    print(get_sum(True))
    print(get_sum(None))
    print(add_some_gold(11000))


