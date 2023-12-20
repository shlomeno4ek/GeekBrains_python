# Задача 25
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

# data = input("Введите символы через пробел: ").split()
# print(data)
# frequency_dict = {}
# for element in data:
#     # print(frequency_dict)
#     if element not in frequency_dict:
#         print(element, end=' ')
#         frequency_dict[element] = 1
#     else:
#         print(f'{element}_{frequency_dict[element]}', end=' ')
#         frequency_dict[element] += 1

# String(str)

# name = "Petr"
#       0123
# print(name[0])
# print(name[0:2])
# print("Petr" < "petr")
# print(name.lower())
# print(name.upper())
# print("pP" == "Pp")
# print([chr(i) for i in range(ord("A"), ord("Z") + 1)])
# print(chr(45))

# Задача 27
text = input("Input text: ").lower()
separator = "!,.?@:;"
for i in separator:
    text = ''.join(text.split(i))
print(len(set(text.split())))