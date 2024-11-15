# https://github.com/CheMax-sudo/python_homework/blob/624fd1447a786a479c611d86a8ed2d9f3aa1deca/work7.py

# Задание 1. Новые списки
# Даны три списка:
# 1. floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
# 2. names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
# 3. numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]
# Напишите код, который создаёт три новых списка. Вот их содержимое:
# 1. Каждое число из списка floats возводится в третью степень и округляется
# до трёх знаков после запятой.
# 2. Из списка names берутся только имена минимум из пяти букв.
# 3. Из списка numbers берётся произведение всех чисел.

from functools import reduce
import time

floats = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers = [22, 33, 10, 6894, 11, 2, 1]

new_floats = list(map(lambda x: round(x ** 3, 3), floats))

new_names = list(filter(lambda x: len(x) >= 5, names))

new_numbers = reduce(lambda x, y: x*y, numbers)

print(f'{new_floats}\n{new_names}\n{new_numbers}')

# Задача 2. Zip
# Даны список букв (letters) и список цифр (numbers). Каждый список состоит из N
# элементов. Создайте кортежи из пар элементов списков и запишите их в список
# results. Не используйте функцию zip. Решите задачу в одну строку (не считая
# print(results)).
# Примеры списков:
# Результат работы программы:
# [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]

let = ['a', 'b', 'c', 'd', 'e']
num = ['1', '2', '3', '4', '5', '6']

result = list(tuple(map(lambda x, y: (x, y), let, num)))
print(result)

# Задача 3. Палиндром
# Используя модуль collections, реализуйте функцию can_be_poly, которая
# принимает на вход строку и проверяет, можно ли получить из неё палиндром.
# Пример кода:
# print(can_be_poly('abcba'))
# print(can_be_poly('abbbc'))
# Результат:
# True
# False

def can_be_poly(str):
    for (i, j) in enumerate(str, 1):
        if j != str[len(str)-i]:
            return False
    return True

print(can_be_poly("abbag"))
str1 = 'abcba'

from collections import Counter

# Counter Класс Counter используется для - подсчета количества каждого элемента в последовательности.

# Метод filter – это встроенный метод в Python для фильтрации элементов последовательности (списка, кортежа, множества и т.п.)

fruits = 'asffowpwlefwpoefkwp'
counter = Counter(fruits)
print(counter)

def can_be_poly(val: str) -> bool:
    char_counts = Counter(val)
    odd_count = len(list(filter(lambda x: x % 2, char_counts.values())))
    return odd_count < 2

print(can_be_poly('eerru')) # Ожидаемый результат: True erure
print(can_be_poly('abbcba')) # Ожидаемый результат: True
print(can_be_poly('abbbc')) # Ожидаемый результат: False abbbc  

# Задача 4. Уникальный шифр

# Напишите функцию, которая принимает строку и возвращает количество
# уникальных символов в строке. Используйте для выполнения задачи
# lambda-функции и map и/или filter.
# Сделайте так, чтобы алгоритм НЕ был регистрозависим: буквы разного
# регистра должны считаться одинаковыми.
# Пример:
# message = "Today is a beautiful day! The sun is shining and the birds are
# singing."
# unique_count = count_unique_characters(message)
# print("Количество уникальных символов в строке:", unique_count)
# Вывод: количество уникальных символов в строке — 5

def count_unique_characters(string):
    # Приводим строку к нижнему регистру, чтобы сделать подсчет регистронезависимым
    lower_string = string.lower()
    # Используем filter для выбора символов, которые встречаются в строке ровно один раз
    unique_chars = list(filter(lambda c: lower_string.count(c.lower()) == 1, lower_string))
    # Выводим уникальные символы (по желанию, можно удалить эту строку)
    print(unique_chars) 
    # Возвращаем количество уникальных символов
    return len(unique_chars)

# # Пример использования:
# message = "Today is a beautiful day! The sun is shining and the birds are singing."
# unique_count = count_unique_characters(message)
# print("Количество уникальных символов в строке:", unique_count)


