documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006', '5400 028765', '5455 002299'],
    '3': []
}
def user_input():
    return input('Введите номер документа ')

def get_people(list_docs,number_doc):
    for item in list_docs:
        if item['number'] == number_doc:
            return item['name']

def get_shelf(list_direct,number_doc):
        for key_v in list_direct:
            if number_doc in list_direct[key_v]:
                return key_v

def result_foo():
    input_command = input('Введите команду ')
    if input_command == 'p':
        some_var = get_people(documents,user_input())
        if some_var:
            print(f"Имя владельца {some_var}")
        else:
            print('Документа нет')
    elif input_command == 's':
        some_var2 = get_shelf(directories, user_input())
        if some_var2:
            print(f"Полка {some_var2}")
        else:
            print('Документа нет')
result_foo()