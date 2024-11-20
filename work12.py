# Урок 12. Семинар. Работа с файлами

# Задание 1. Сумма чисел
# Во входном файле numbers.txt записано N целых чисел, которые могут быть
# разделены пробелами и концами строк. Напишите программу, которая выводит
# сумму чисел во выходной файл answer.txt.
# Пример:
# Содержимое файла numbers.txt
# 2
#   2
# 2
#    2
# Содержимое файла answer.txt
# 8

sum = 0
data = open('numbers.txt', 'r')
for i in data:
    sum += int(i)
data = open('answer.txt', 'w+') # здесь указываем режим, в котором будем работать
data.writelines(str(sum)) # разделителей не будет
data.close()

sum = 0
with open('numbers.txt', 'r') as data1:   
    for i in data1:
        sum += int(i)
    data1 = open('answer.txt', 'w+')
    data1.writelines(str(sum))
    
# Задание 2. Сумма чисел
# В файле zen.txt хранится так называемый Дзен Пайтона — текст философии
# программирования на языке Python. Выглядит он так:

# Напишите программу, которая выводит на экран все строки этого файла в
# обратном порядке.
# Кстати, попробуйте открыть консоль Python и ввести команду import this.
# Результат работы программы:

# Namespaces are one honking great idea -- let's do more of those!
# If the implementation is easy to explain, it may be a good idea.
# If the implementation is hard to explain, it's a bad idea.
# Although never is often better than *right* now.

data = open('zen.txt', 'r')
lines = data.readlines() # Функция readlines() Вернёт список строк.
for line in reversed(lines): # С помощью функции reversed переворачиваем строку line и получаем объекты(перевёрнутого списка)
    print(line.strip()) # strip() Удаляет пробелы между строк
data.close()

# Задача 3. Турнир

# В файле first_tour.txt записано число K и данные об участниках турнира по
# настольной игре «Орлеан»: фамилии, имена и количество баллов, набранных в
# первом туре. Во второй тур проходят участники, которые набрали более K
# баллов в первом туре.
# Напишите программу, которая выводит в файл second_tour.txt данные всех
# участников, прошедших во второй тур, с нумерацией.
# В первой строке нужно вывести в файл second_tour.txt количество участников
# второго тура. Затем программа должна вывести фамилии, инициалы и
# количество баллов всех участников, прошедших во второй тур, с нумерацией.
# Имя нужно сократить до одной буквы. Список должен быть отсортирован по
# убыванию набранных баллов.

# Пример:
# Содержимое файла first_tour.txt:
# 80
# Ivanov Serg 80
# Sergeev Petr 92
# Petrov Vasiliy 98
# Vasiliev Maxim 78
# Содержимое файла second_tour.txt:
# 2
# 1) V. Petrov 98
# 2) P. Sergeev 92
   
with open('first_tour.txt', 'r') as data:
    data = data.readlines()
    data = [item.strip() for item in data]
    k = int(*data[:1])
    list_gamer = data[1:len(data)]
    list_gamer = sorted(list_gamer, key=lambda x: x[-2:], reverse=True)

    second_list = []
    caunt = 0

    data_two = open('answer.txt', 'w')
    for i in list_gamer:
        if int(k) < int(i[len(i)-2:]):
            caunt += 1
            i = i.split()
            res = str(f'{caunt}) {i[1][0:1]}. {i[0]} {i[2]}\n')       
            data_two.writelines(str(res))        
    data_two.close()        

# Задача 4. Частотный анализ
# Есть файл text.txt, который содержит текст. Напишите программу, которая
# выполняет частотный анализ, определяя долю каждой буквы английского
# алфавита в общем количестве английских букв в тексте, и выводит результат в
# файл analysis.txt. Символы, не являющиеся буквами английского алфавита,
# учитывать не нужно.
# В файл analysis.txt выводится доля каждой буквы, встречающейся в тексте, с
# тремя знаками в дробной части. Буквы должны быть отсортированы по
# убыванию их доли. Буквы с равной долей должны следовать в алфавитном
# порядке.
# Пример:
# Содержимое файла text.txt:
# Mama myla ramu.
# Содержимое файла analysis.txt:
# a 0.333
# m 0.333
# l 0.083
# r 0.083
# u 0.083
# y 0.083

import re

def clean_string(word):
        return re.sub(r"[`!?.:;,'\"()-]", "", word.strip())

with open('text.txt', 'r') as file:
    data_a = ''.join(file.read().lower().split())
    new_data = list(filter(None, map(clean_string, data_a)))
    res = {}
    res2 = ' '
    for i in new_data:
      res[i] = res.get(i, 0) + 1
    data_a2 = open('analysis.txt', 'w')
    for key, value in res.items():
      value = round(value / len(new_data), 3)
      res2 = (f'{key} {value}\n')
      data_a2.writelines(res2)


# Задача 5*. «Война и мир»
# Мало кто не знает знаменитый роман Л. Н. Толстого «Война и мир». Это
# довольно объёмное произведение лежит в архиве voina-i-mir.zip. Напишите
# программу, которая подсчитывает статистику по буквам (не только русского
# алфавита) в этом романе и выводит результат на экран (или в файл). Результат
# должен быть отсортирован по частоте встречаемости букв (по возрастанию или
# убыванию). Регистр символов имеет значение.
# Архив можно распаковать вручную, но, если хотите, можете изучить
# документацию по модулю zipfile (можно использовать и другой модуль) и
# попробовать написать код, который будет распаковывать архив за вас.

import zipfile

archive_path = 'voina-i-mir.zip'
# Открываем архив
with zipfile.ZipFile(archive_path, 'r') as archive:
    # Получаем список всех файлов внутри архива
    files_in_zip = archive.namelist()
    for file in files_in_zip:
        if file.endswith('.txt'):
            with archive.open(file) as txt_file:
                content = txt_file.read().decode('utf-8')
                print(f"Файл {file}:")
                print(content)
