# nums = [int(i) for i in input().split()]
# max = max(nums)
# min = min(nums)
# for i in range(len(nums)):
#     if nums[i] == max:
#         nums[i] = min
# print(nums)
# 

# тоже самое но короче 
# marks = [int(i) for i in input("Введите оценки: ").split()]
# print(*[min(marks) if i == max(marks) else i for i in marks])

def f(n):
    
    if n == 0:
        return ''
    a = input()
    return f(n-1) + f'{a} '
print(f(2))