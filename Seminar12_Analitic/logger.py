from data_create import name_data, surname_data, phone_data, address_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input("В каком формате записывать данные\n\n"
                    f"1 Вариант\n"
                    f"{name}\n{surname}\n{phone}\n{address}\n\n"
                    f"2 Вариант\n"
                    f"{name};{surname};{phone};{address}\n"
                    f"Выберите вариант: "))
    while var < 1 and var > 2:
        print("Неправильный ввод")
        var = int(input('Введите число '))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")


def print_data():
    print('Вывожу данные из 1 файла: \n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j = i
        print(''.join(data_first_list))


    print('Вывожу данные из 2 файла: \n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        print(*data_second)

def edit_data():
    print_data()
    n = int(input("В каком файле хотите изменить данные: "))
    
    while n < 1 or n > 2:
        print("Неправильный ввод")
        n = int(input('Введите номер файла: '))

    if n == 1:
        with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
            data_file = f.readlines()
            
        for i in range(len(data_file)):
            print(f'{i + 1} - {data_file[i]}') 
        number = int(input("Какую строку хотите изменить: "))

        while number < 1 or number > len(data_file) or data_file[number - 1] == "\n":
            print("Неправильный ввод")
            number = int(input('Введите номер строки: '))

        text = input("Введите новые данные: ")
        data_file[number - 1] = f'{text}\n'

        with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
            f.writelines(data_file) 
    else:
        with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
            data_file = f.readlines()   
            
        for i in range(len(data_file)):
            print(f'{i + 1} - {data_file[i]}') 
        number = int(input("Какую строку хотите изменить: "))

        while number < 1 or number > len(data_file) or data_file[number - 1] == "\n":
            print("Неправильный ввод")
            number = int(input('Введите номер строки: '))
        
        k = 1
        for i in data_file[number - 1].split(';'):
            print(f'{k} - {i}')
            k += 1
        number_parametr = int(input("Под каким номером хотите изменить знаачение: "))
        while number_parametr < 1 or number_parametr > len(data_file[number - 1].split(';')):
            print("Неправильный ввод")
            number_parametr = int(input('Введите номер строки: '))
        text = input("Введите новые данные: ")

        k = 1
        data = list()
        for i in data_file[number - 1].split(';'):
            if k == number_parametr:
                data.append(text)
            else :
                data.append(i)
            k += 1
        data_file[number - 1] = ';'.join(data)
        with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
            f.writelines(data_file)
        
def delete_data():
    print_data()
    n = int(input("В каком файле хотите удалить данные: "))
    
    while n < 1 or n > 2:
        print("Неправильный ввод")
        n = int(input('Введите номер файла: '))
    
    if n == 1:
        with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
            data_file = f.readlines()

        k = 1    
        for i in range(len(data_file)):
            if data_file[i] == '\n':
                k += 1
            print(f'{k} - {data_file[i]}') 
        number = int(input("Какую запись хотите уалить: "))

        while number < 1 or number > len(data_file):
            print("Неправильный ввод")
            number = int(input('Введите номер строки: '))

        k = 1    
        for i in range(len(data_file)):
            if data_file[i] == '\n':
                k += 1
            if k == number:
                del data_file[i]
                del data_file[i]
                del data_file[i]
                del data_file[i]
                break

        with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
            f.writelines(data_file) 
    else:
        with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
            data_file = f.readlines()
            
        for i in range(len(data_file)):
            print(f'{i + 1} - {data_file[i]}') 
        number = int(input("Какую строку хотите уалить: "))

        while number < 1 or number > len(data_file) or data_file[number - 1] == "\n":
            print("Неправильный ввод")
            number = int(input('Введите номер строки: '))

        del data_file[number - 1]

        with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
            f.writelines(data_file) 
