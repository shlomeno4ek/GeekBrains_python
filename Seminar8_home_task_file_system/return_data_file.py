from choice_file import choice_number_file


def data_file():
    nf = choice_number_file()
    with open(f'db/data_{nf}.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    return data, nf

# def data_from_copy_file():
#     nf1 = choice_from_number_file()

#     with open(f'db/data_{nf1}.txt', 'r', encoding='utf-8') as file:
#         data = file.readlines()

#     return data, nf
