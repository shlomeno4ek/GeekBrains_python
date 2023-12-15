# Задача 8
# n = int(input("Введите кол-во долек по горизонтали: "))
# m = int(input("Введите кол-во долек по вертикали: "))
# k = int(input("Введите кол-во долек, которое нужно отломить: "))
# if k < n * m and (k % n == 0 or k % m == 0):
#     print('yes')
# else:
#     print('no')


# Цикл(for)
# for element in 1, 56, -2, 4.56, "Ivan", True, False:
#     print(element * 2, end=' ')

# Функция(range)
# range(initial=0, end(обязательное), step=+1)
# print(type(range(5)))

# print(*range(6))
# print(*range(2, 8, 2))
# print(*range(5, 0, -1))
# print(*range(2, 7))
# from numpy import arange # pip install numpy

# print(type(arange(5, 0)))


# for i in range(5):
#     print(i)


# Задача 9
# n = int(input("Введите число: "))
# i = 2
# result = 1
# while i <= n:
#     result = result * i
#     i = i + 1
# print(result)


# Задача 11
# f(n) = f(n - 1) + f(n - 2)
# 0 1 1 2 3 5 8 13 21 34 
# n = int(input("Введите число: "))
# a0 = 0
# a1 = 1
# for i in range(n): # n = 5 range(5) = [0, 1, 2, 3, 4]
#     print(a0, end=' ')
#     a_next = a0 + a1
#     a0 = a1
#     a1 = a_next


# n = int(input("Введите число: "))
# a_next = 0
# a0 = 0
# a1 = 1
# i = 2
# while a_next < n: # a_next = n or a_next > n
#     a_next = a0 + a1
#     a0 = a1
#     a1 = a_next
#     i = i + 1
# if a_next > n:
#     i = -1
# print(i)


# Задача 15
# n = int(input("Введите кол-во арбузов: ")) # n = 5
# x = int(input("Введите массу 1-го арбуза: "))
# min_massa = x
# max_massa = x
# for i in range(n - 1): # 0 1 2 3 ... n - 2
#     x = int(input(f"Введите массу {i + 2}-го арбуза: "))
#     if min_massa > x:
#         min_massa = x
#     elif max_massa < x:
#         max_massa = x
# print(min_massa, max_massa)


# Задача 13
n = int(input("Введите кол-во дней: "))
count_max = 0
count = 0
for i in range(n):
    temp = int(input(f'Введите температуру {i + 1}-го дня: '))
    if temp > 0:
        count = count + 1
    else:
        if count_max < count:
            count_max = count
        count = 0
print(count_max)