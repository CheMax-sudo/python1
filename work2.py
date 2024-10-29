# Урок 2. Циклы (for, while)
# Задание 1: Поставьте оценку!

# Вася выложил своё новое приложение на платформу для начинающих разработчиков,
# на ней пользователи могут ставить оценку приложению: от −100 до 100. Ему
# захотелось сравнить количество положительных и отрицательных отзывов, для этого
# он заранее отфильтровал все отзывы так, чтобы в конце были те, которые равны нулю.
# Напишите программу, которая находит количество положительных и количество
# отрицательных чисел в последовательности. Последовательность заканчивается на
# числе 0.
# Пример:
# Введите число: −4
# Введите число: −90
# Введите число: 6
# Введите число: 0
# Кол-во положительных чисел: 1
# Кол-во отрицательных чисел: 2

count_plus = 0
count_minus = 0
while True:
    n = int(input("Введите число: "))
    if n < 0:
        count_minus += 1
    elif n > 0:    
        count_plus += 1
    else:
        break
print(f'Кол-во положительных чисел: {count_plus}\nКол-во отрицательных чисел: {count_minus}')    

# Задача 2. Обычный день на работе
# Максим программирует целый день на работе и вечером идёт домой. Каждый час
# начальство кидает ему несколько задач, которые нужно решить до следующего
# рабочего часа. Вдобавок каждый час Максиму звонит супруга. Он знает, что если он
# возьмёт трубку, то жена попросит зайти вечером в магазин.
# Напишите программу, в которой считается, сколько задач выполнил Максим за день
# (восемь часов). Если он хотя бы раз взял трубку, то в конце дополнительно выводите
# сообщение: «Нужно зайти в магазин».
# Пример
# Начался восьмичасовой рабочий день.
# 1-й час
# Сколько задач решит Максим? 1
# Звонит жена. Взять трубку? (1 — да, 0 — нет): 0
# 2-й час
# Сколько задач решит Максим? 2
# Звонит жена. Взять трубку? (1 — да, 0 — нет): 0
# 3-й час
# Сколько задач решит Максим? 3
# Звонит жена. Взять трубку? (1 — да, 0 — нет): 0
# 4-й час
# Сколько задач решит Максим? 4
# Звонит жена. Взять трубку? (1 — да, 0 — нет): 1
# 5-й час
# Сколько задач решит Максим? 5
# Звонит жена. Взять трубку? (1 — да, 0 — нет): 0
# 6-й час
# Сколько задач решит Максим? 1
# Звонит жена. Взять трубку? (1 — да, 0 — нет): 0
# 7-й час
# Сколько задач решит Максим? 2
# Звонит жена. Взять трубку? (1 — да, 0 — нет): 1
# 8-й час
# Сколько задач решит Максим? 3
# Звонит жена. Взять трубку? (1 — да, 0 — нет): 0
# Рабочий день закончился. Всего выполнено задач: 21
# Нужно зайти в магазин.

count_task = 0
go_shop = ""

for i in range(8):
    num_task = int(input("Сколько задач решит Максим?: "))
    n = int(input("Звонит жена. Взять трубку? (1 — да, 0 — нет): "))
    if n == 0:
        count_task += num_task        
    elif n == 1:
        count_task += num_task
        go_shop = "Нужно зайти в магазин."
    else:
        print("Ввод не корректен, попробуйте сначала!")
        
print(f'Рабочий день закончился. Всего выполнено задач: {count_task}\n{go_shop}')    

import random

# Задача 3. Игра «Угадай число»

# Папа-программист написал для сына программу, которая просит его угадать
# число. Недостаток программы был в том, что бедному сыну приходилось её
# каждый раз перезапускать, чтобы угадывать число. Теперь, когда мы знаем
# гораздо больше, пришло время исправить этот недостаток и заодно немного
# улучшить саму игру.
# Напишите программу-игру, которая запрашивает у пользователя число до тех
# пор, пока он его не отгадает. Выводите сообщения в соответствии с примером.

# Пример (загадали число 7)
# Введите число: 3
# Число меньше, чем нужно. Попробуйте ещё раз!
# Введите число: 10
# Число больше, чем нужно. Попробуйте ещё раз!
# Введите число: 8
# Число больше, чем нужно. Попробуйте ещё раз!
# Введите число: 7
# Вы угадали! Число попыток: 4 

num_rnd = random.randint(1, 10)
count = 0
while True:
    answer = int(input("Введите число: "))
    count += 1
    if answer == num_rnd:
        print(f'Вы угадали! Число попыток: {count}')
        break
    elif answer < num_rnd:
        print("Число больше, чем нужно. Попробуйте ещё раз!")
    elif answer > num_rnd:
        print("Число меньше, чем нужно. Попробуйте ещё раз!")    


# Задача 4. Посчитай чужую зарплату...

# Бухгалтер устала постоянно считать вручную среднегодовую зарплату
# сотрудников компании и, чтобы облегчить себе жизнь, обратилась к
# программисту.
# Напишите программу, которая принимает от пользователя зарплату сотрудника
# за каждый из 12 месяцев и выводит на экран среднюю зарплату за год

sum = 0
months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
for i in months:
    n = (int(input(f'Введите зарплату за {i}: ')))
    sum += n
average = sum/len(months)    
print(int(average)) 


# Задача 5. Пропавшая карточка

# Для настольной игры используются карточки с номерами от 1 до N. Одна
# карточка потерялась. Напишите программу, которая поможет найти потерянную
# карточку, если номера оставшихся известны. Найдите её, зная номера
# оставшихся карточек.
# Введите число карточек — N.
# Затем введите N − 1 номера оставшихся карточек. 
# Они могут быть введены в любом порядке.

list_1 = []  
list_2 = []
quantity = int(input("Введите количество карточек: "))
for i in range(1, quantity+1):
     list_1.append(i)
for j in range(quantity-1):
    num = int(input("Введите число карточки: ")) 
    list_2.append(num)
result = list(set(list_1)-set(list_2))    
print(*result)    
                  
# Задача 6 *. Кинотеатр

# X мальчиков и Y девочек пошли в кинотеатр и купили билеты на идущие подряд
# места в одном ряду. Напишите программу, которая выдаст, как нужно сесть
# мальчикам и девочкам, чтобы рядом с каждым мальчиком сидела хотя бы одна
# девочка, а рядом с каждой девочкой — хотя бы один мальчик.
# На вход подаются два числа: количество мальчиков X и количество девочек Y.
# В ответе выведите какую-нибудь строку, в которой будет ровно X символов B,
# обозначающих мальчиков, и Y символов G, обозначающих девочек,
# удовлетворяющую условию задачи. Пробелы между символами выводить не
# нужно. Если рассадить мальчиков и девочек согласно условию задачи
# невозможно, выведите строку «Нет решения»

boys = int(input("Введите количество М: "))
girls = int(input("Введите количество Д: "))

answer = ""
if boys >= girls:
    n = boys
else:   
    n = girls

if boys == girls:
    answer = "BG"*n       
elif boys - girls == 1 or girls - boys == 1:
    if boys > girls:
        answer = "BG"*girls+"B"
    else:
        answer = "GB"*boys+"G"
else:
    print("Нет решения.")
print(answer)     