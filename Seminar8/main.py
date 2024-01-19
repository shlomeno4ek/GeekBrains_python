file = open('data1.txt', 'r', encoding='utf-8')
print(file.readlines())
file.close()

def clear_and_write():
    with open('data1.txt', 'r', encoding='utf-8') as file:
        file.write('Anna\n')

def append_row():
    with open('data1.txt', 'w', encoding='utf-8') as file:
        file.write('Ivan\n')
    