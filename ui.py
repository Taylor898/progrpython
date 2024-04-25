from logger import input_data, print_data, delete_data, update_data


def interface():
    print("Выберите вариант из предложенных: \n 1 - запись данных  \n 2 - вывод данных \n 3 - изменение данных \n 4 - удаление данных")
    command = int(input())

    while command not in range(1,5):
        print("неправильный ввод")

    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        update_data()
    elif command == 4:
        delete_data()