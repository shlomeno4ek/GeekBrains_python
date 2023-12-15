# Видры трансляций программного кода:
# 1. Компиляция(С#, C++ ...)
# 2. Интерпретация(Python, JavaScript...)

# C#:
# int n = 5; -> []

# Python
# n = 5 -> class <'int'> -> []


# name = input("Введите имя: ") # str(string)
# print(name)



# name = input("Введите имя: ")
# age = input("Введите свой возраст: ")
# print(name + " " + age)
# print(f'Привет, {name}! Тебе {age} лет.') # f-строки или форматированный вывод

# name = 'Sidor'
# print(type(name)) # <class 'str'>
# number = 123
# print(type(number)) # <class 'int'>
# float_number = 334.192
# print(type(float_number)) # <class 'float'>


# n = input("Введите число: ") # "234"
# print(type(n)) 

# Встроенные функции(int, float, str)
# print(int("234") + 6)
# print(int(3.99))
# print(int("234"))
# # print(int("23 4")) ValueError: invalid literal for int() with base 10: '23 4'
# print(float(56))
# print(str(45.56) * 2)
# print(str(12) * 2)

# n = int(input("Введите 1-ое число: "))
# m = int(input("Введите 1-ое число: "))
# print(type(n))
# print(f'{n} + {m} = {n + m}')
# print(f'{n} - {m} = {n - m}')
# print(f'{n} * {m} = {n * m}')
# print(f'{n} : {m} = {n // m}(ост. {n % m})')
# print(f'{n} : {m} = {n / m}')
# print(f'{n}^{m} = {n ** m}')


# print(7 > 5)
# print(10 < 0)
# condition -> True or False


# Алгебра логики(Булевская Алгебра) True(1) False(0)

# конъюнкция(логическое умножение) - and
# дизъюнкция(логическое сложение) - or
# отрицание(обратное значение) - not

# print(7 > 5 and 10 < 0)
# #      1  *   0 = 0(False)

# print(1 > 2 or 5 > -1)
# #      0    +    1 = 1

# print(3 > 2 or 5 > 2)
# #      1    +    1 = 1

# print((3 > 2 or 5 > 3) and 2 < 0)


# Задача 1

# n = int(input("Сколько за день проезжает машина? - "))
# m = int(input("Общее расстояние: "))
# # 750 : 700 = 1(ост. 50) + 1
# # 2100 : 700 = 3 (ост. 0) + 0
# print((m + n - 1) //  n)
# (m + n - 1) // n
# (1401 + 700 - 1) // 700 = 3
# print(-12 % 5) # 15 - 12 = 3
# print(-14 % 6) # 18 - 14
# print(-7 % 3) # 9 - 7


# Задача 3
# a = 20
# b = 21 # 21 // 2 = 10  21 % 2 = 1
# c = 22
# print(a // 2 + a % 2 + b // 2 + b % 2 + c // 2 + c % 2)


# Задача 5
# i = 3
# j = 4
# if i == j:
#     print("Не хватает данных")
# else:
#     print(i + j - 1)


# Задача 7

year = int(input("Введите год: "))
print(year % 4 == 0 and year % 100 != 0 or year % 400 == 0)