from return_data_file import data_file

def copy_row():
    data, nf = data_file()
    count_rows = len(data)
    if count_rows == 0:
        print("Файл пустой!")
    else:
        number_row = int(input(f"Введите номер строки, которую хотите скопировать"
                               f"от 1 до {count_rows}: "))
        while number_row < 1 or number_row > count_rows:
            number_row = int(input(f"Ошибка!"
                                   f"Введите номер строки, которую хотите скопировать"
                                   f"от 1 до {count_rows}: "))
        with open(f'db/data_{3 - nf}.txt', 'a', encoding='utf-8') as file2:
            file2.write(data[number_row - 1])
        
        print("Строка успешно скопирована!")
    return