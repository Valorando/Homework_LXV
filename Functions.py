def Add_employee_to_list(path_to_file, employee):
    try:
        with open(f'{path_to_file}', 'a', encoding='utf-8') as file:
            file.write(f'{employee.first_name} {employee.second_name} {employee.age}\n')
            print(f'{employee.first_name} {employee.second_name} {employee.age} успешно добавлен(на) в список')

            Save_result_to_file(f'Была выполнена операция добавления в файл {path_to_file}, данные: {employee.first_name} {employee.second_name} {employee.age}\n')
    except Exception as e:
        print(f"Ошибка при добавлении сотрудника: {e}")



def Edit_employee_information(path_to_file, old_employee, new_employee):
    try:
        with open(f'{path_to_file}', 'r', encoding='utf-8') as file:
            lines = file.readlines()

        with open(f'{path_to_file}', 'w', encoding='utf-8') as file:
            replaced = False
            for line in lines:
                if old_employee.first_name + ' ' + old_employee.second_name + ' ' + str(old_employee.age) in line:
                    file.write(str(new_employee.first_name) + ' ' + str(new_employee.second_name) + ' ' + str(new_employee.age) + '\n')
                    replaced = True
                    print(f"Информация о сотруднике {old_employee.first_name} {old_employee.second_name} {old_employee.age} успешно обновлена на {new_employee.first_name} {new_employee.second_name} {new_employee.age}")

                    Save_result_to_file(f'Была выполнена операция редактирования в файле {path_to_file}, старые данные: {old_employee.first_name} {old_employee.second_name} {old_employee.age} - новые данные: {new_employee.first_name} {new_employee.second_name} {new_employee.age}\n')
                else:
                    file.write(line)
            if not replaced:
                print(f"Сотрудник {old_employee.first_name} {old_employee.second_name} {old_employee.age} не найден(на)")
    except Exception as e:
        print(f"Ошибка при редактировании информации о сотруднике: {e}")



def Delete_employee_on_list(path_to_file, employee):
    try:
        with open(f'{path_to_file}', 'r', encoding='utf-8') as file:
            lines = file.readlines()

        with open(f'{path_to_file}', 'w', encoding='utf-8') as file:
            removed = False
            for line in lines:
                if employee.first_name + ' ' + employee.second_name + ' ' + str(employee.age) not in line:
                    file.write(line)
                else:
                    removed = True
            if removed:
                print(f"Сотрудник {employee.first_name} {employee.second_name} {employee.age} успешно удален(на)")

                Save_result_to_file(f'Была выполнена операция удаления в файле {path_to_file}, данные: {employee.first_name} {employee.second_name} {employee.age}\n')
            else:
                print(f"Сотрудник {employee.first_name} {employee.second_name} {employee.age} не найден(на)")
    except Exception as e:
        print(f"Ошибка при удалении сотрудника: {e}")



def Display_all_employees(path_to_file):
    try:
        with open(f'{path_to_file}', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                print(line, end='')

        Save_result_to_file(f'Была выполнена операция получения всех данных в файле {path_to_file}, данные:\n {", ".join([line.strip() for line in lines])}\n')
    except Exception as e:
        print(f"Ошибка при отображении сотрудников: {e}")



def Search_employee_on_list(path_to_file, keyword):
    try:
        with open(f'{path_to_file}', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            found = False
            for line in lines:
                if keyword.lower() in line.lower():
                    print(line, end='')
                    found = True

            if found:
                Save_result_to_file(f'Была выполнена операция поиска в файле {path_to_file}, ключевое слово: {keyword}, данные:\n {", ".join([line.strip() for line in lines if keyword.lower() in line.lower()])}\n')
            else:
                print(f"Сотрудники с ключевым словом '{keyword}' не найдены")
    except Exception as e:
        print(f"Ошибка при поиске сотрудника: {e}")



def Save_result_to_file(result):
    try:
        with open('employees_log.txt', 'a', encoding='utf-8') as file:
            file.write(f'{result}')
            print("Действие сохранено в employees_log.txt находящийся в директории программы")
    except Exception as e:
        print(f"Ошибка при сохранении: {e}")
