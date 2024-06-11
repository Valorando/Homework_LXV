import os
import Functions
import Model

print("Добро пожаловать, прежде чем начать работу вы должны подключить файл со списком сотрудников")
print("Если файл находится в директории программы, то вам нужно указать только его название")
print("Если файл находится в другой директории, вам необходимо дополнительно указать путь к нему")

while True:
    path_to_file = input("Введите путь к файлу: ")
    if os.path.isfile(path_to_file):
        print("Файл успешно загружен")
        break
    else:
        print("Файл не найден")
        key = int(input("Хотите ввести путь к файлу снова? Введите 0 если да или введите что-то другое если нет: "))
        if key != 0:
            print("Выход из программы...")
            exit(0)

while True:
    print("\nМеню управления списком сотрудников:")
    print("1 - Добавить сотрудника в список")
    print("2 - Редактировать информацию о сотруднике")
    print("3 - Удалить сотрудника из списка")
    print("4 - Показать всех сотрудников")
    print("6 - Найти сотрудника в списке")
    print("7 - Выйти")
    
    try:
        key = int(input("Для выбора интересующей вас опции введите её номер и нажмите Enter: "))
    except ValueError:
        print("Неверный ввод Пожалуйста, введите число")
        continue

    if key == 1:
        employee = Model.Employee()
        employee.first_name = input("Введите имя: ")
        employee.second_name = input("Введите фамилию: ")
        employee.age = int(input("Введите возраст: "))
        Functions.Add_employee_to_list(path_to_file, employee)

    elif key == 2:
        old_employee = Model.Employee()
        old_employee.first_name = input("Введите старое имя: ")
        old_employee.second_name = input("Введите старую фамилию: ")
        old_employee.age = int(input("Введите старый возраст: "))

        new_employee = Model.Employee()
        new_employee.first_name = input("Введите новое имя: ")
        new_employee.second_name = input("Введите новую фамилию: ")
        new_employee.age = int(input("Введите новый возраст: "))
        Functions.Edit_employee_information(path_to_file, old_employee, new_employee)

    elif key == 3:
        employee = Model.Employee()
        employee.first_name = input("Введите имя для удаления: ")
        employee.second_name = input("Введите фамилию для удаления: ")
        employee.age = int(input("Введите возраст для удаления: "))
        Functions.Delete_employee_on_list(path_to_file, employee)

    elif key == 4:
        Functions.Display_all_employees(path_to_file)
        
    elif key == 6:
        keyword = input("Введите ключевое слово для поиска: ")
        Functions.Search_employee_on_list(path_to_file, keyword)

    elif key == 7:
        print("Выход из программы...")
        exit(0)
    else:
        print("Неверный ввод. Пожалуйста, выберите корректный номер опции")
