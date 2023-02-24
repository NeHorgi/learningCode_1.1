from time import perf_counter
from typing import List, Any
from functools import wraps


'''
Задача реализовать декоратор, который будет считать время
работы декорируемой функции и выводить его в формате
ЧЧ:ММ:СС.МС
'''


#Реализация декоратора - берем точку отсчета начала работы функции и после вычитаем ее из того времени,
#которое будет, когда функция закончит работу
def timer(func: Any) -> None:
    def wrapper(*args):
        start = perf_counter()
        result = func(*args)
        print(perf_counter() - start)
        return result
    return wrapper


#Честно говоря, я не очень понял, как мне может тут помочь библиотека functools, тем более, что моя вариация
#декоратора работает даже точнее
def functools_timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args)
        print(perf_counter() - start)
        return result
    return wrapper


'''
В качесте "подопытного" взята задача с LeetCode, которая мне компьютер уронила из-за слишком долгого выполнения, 
при первой попытке решить ее.
Само условие звучит следующим образом:
169. Majority Element
Given an array nums of size n, return the majority element. 
The majority element is the element that appears more than n / 2 times. Мажорити элемент - элемент, что встречается больше, чем n / 2 раз 
You may assume that the majority element always exists in the array.
'''


@functools_timer
@timer
def majorityElement(nums: List[int]) -> int:
        set_list = set(nums)
        majority_element = 0
        majority_count = 0
        for element in set_list:
            if nums.count(element) > majority_count:
                majority_count = nums.count(element)
                majority_element = element
        return majority_element


#Достаточно большой массив данных, так как мелкие массивы функция щелкает за доли мили-секунд
check = [i for i in range(1, 10000)]


if __name__ == '__main__':
    print(majorityElement(check))
