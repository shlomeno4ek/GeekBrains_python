# Задача 17
# print([i for i in range(5)])
# print([(i, i ** 2) for i in range(5)])

# print([i for i in range(11) if i % 2 == 0])
# input() ->   "-10 23 5 4 89 23"
# input().split() -> ["-10", "23", "5", "4", "89", "23"]
# for i in input().split():
#     print(int(i) * 2)

# data = [int(i) for i in input("Введите числа: ").split()]
# print(len(set(data)))
# data = ["-10", "23", "5", "4", "89", "23"]
# print(" !! ".join(data))

# Задача 19
# data = [int(i) for i in input("Введите числа: ").split()]
# k = int(input("Введите кол-во сдвигов: ")) % len(data)
# for i in range(k):
#     data.insert(0, data.pop(-1))
#     # [5, 1, 2, 3, 4] k = 2
#     # data.pop(-1) -> 4
#     # data.insert(0, 4)
#     # [4, 5, 1, 2, 3]
# print(data)

# Задача 21

# data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": "S005"}, {"V ":"S009"}, {"VIII":"S007 "}]
# # print(data[0]["V"])
# result = set()  # = {} dictionary
# for d in data:
#     for key in d:
#         result.add(d[key])
# print(result)

# Задача 23
# Мой вариант
# data = [int(i) for i in input("Введите числа: ").split()]
# count = 0
# for i in range(len(data)- 1):
#     if data[i] < data[i + 1]:
#         count += 1
# print(count)

# Вариант преподователя
data = [int(i) for i in input("Введите числа: ").split()]
result = [data[i - 1] < data[i] for i in range(1, len(data))] 
print(sum(result)) # складываем все элементы списка

