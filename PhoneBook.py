# Телефонная книга
# Функции:
# 1. Импортировать данные из файла
# 2. Экспортировать данные в файл
# 3. Добавить запись
# 4. Поиск по фамилии или имени
# 5. Изменить запись
# 6. Удалить запись
# 7. Вывести все записи

def import_data(file_name):
    try:
        with open(file_name, "r") as file:
            for line in file:
                data = line.strip().split(", ")
                phone_book[data[0]] = {
                    "Имя": data[1],
                    "Отчество": data[2],
                    "Номер телефона": data[3]
                }
    except FileNotFoundError:
        print("Файл не найден.")

def export_data(file_name):
    with open(file_name, "w") as file:
        for last_name, entry in phone_book.items():
            file.write(
                last_name + ", " +
                entry["Имя"] + ", " +
                entry["Отчество"] + ", " +
                entry["Номер телефона"] + "n"
            )

def add_data():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    middle_name = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")
    phone_book[last_name] = {
        "Имя": first_name,
        "Отчество": middle_name,
        "Номер телефона": phone_number
    }
    print("Запись успешно добавлена.")

def search_data(term):
    results = []
    for last_name, entry in phone_book.items():
        if term.lower() in last_name.lower() or term.lower() in entry["Имя"].lower():
            results.append((last_name, entry))
    return results

def modify_entry():
    term = input("Введите фамилию или имя записи, которую хотите изменить: ")
    results = search_data(term)
    if len(results) == 0:
        print("Запись не найдена.")
    elif len(results) == 1:
        last_name, entry = results[0]
        print("Найдена следующая запись:")
        print_entry(last_name, entry)
        field = input("Введите поле, которое хотите изменить (Фамилия, Имя, Отчество, Номер телефона): ")
        new_value = input("Введите новое значение: ")
        entry[field] = new_value
        print("Запись успешно изменена.")
        print_entry(last_name, entry)
    else:
        print("Найдено несколько записей:")
        for i, (last_name, entry) in enumerate(results):
            print(f"{i + 1}.")
            print_entry(last_name, entry)
        choice = int(input("Введите номер записи, которую хотите изменить: ")) - 1
        last_name, entry = results[choice]
        field = input("Введите поле, которое хотите изменить (Фамилия, Имя, Отчество, Номер телефона): ")
        new_value = input("Введите новое значение: ")
        entry[field] = new_value
        print("Запись успешно изменена.")
        print_entry(last_name, entry)

def delete_entry():
    term = input("Введите фамилию или имя записи, которую хотите удалить: ")
    results = search_data(term)
    if len(results) == 0:
        print("Запись не найдена.")
    elif len(results) == 1:
        last_name, entry = results[0]
        print("Найдена следующая запись:")
        print_entry(last_name, entry)
        confirm = input("Вы уверены, что хотите удалить данную запись? (Да/Нет): ")
        if confirm.lower() == "да":
            del phone_book[last_name]
            print("Запись успешно удалена.")
    else:
        print("Найдено несколько записей:")
        for i, (last_name, entry) in enumerate(results):
            print(f"{i + 1}.")
            print_entry(last_name, entry)
        choice = int(input("Введите номер записи, которую хотите удалить: ")) - 1
        last_name, entry = results[choice]
        confirm = input("Вы уверены, что хотите удалить данную запись? (Да/Нет): ")
        if confirm.lower() == "да":
            del phone_book[last_name]
            print("Запись успешно удалена.")

def print_entry(last_name, entry):
    print("Фамилия:", last_name)
    print("Имя:", entry["Имя"])
    print("Отчество:", entry["Отчество"])
    print("Номер телефона:", entry["Номер телефона"])

def print_phone_book():
    if len(phone_book) > 0:
        for last_name, entry in phone_book.items():
            print_entry(last_name, entry)
            print()
    else:
        print("Телефонный справочник пуст.")

phone_book = {}
while True:
    print("Меню:")
    print("1: Импортировать данные из файла")
    print("2: Экспортировать данные в файл")
    print("3: Добавить запись")
    print("4: Поиск по фамилии или имени")
    print("5: Изменить запись")
    print("6: Удалить запись")
    print("7: Вывести все записи")
    print("8: Выйти")
    choice = input("Введите номер пункта меню: ")

    if choice == "1":
        file_name = input("Введите имя файла: ")
        import_data(file_name)

    elif choice == "2":
        file_name = input("Введите имя файла: ")
        export_data(file_name)
    elif choice == "3":
        add_data()
    elif choice == "4":
        term = input("Введите фамилию или имя для поиска: ")
        results = search_data(term)
        if len(results) > 0:
            print("Результаты поиска:")
            for i, (last_name, entry) in enumerate(results):
                print(f"{i + 1}.")
                print_entry(last_name, entry)
                print()
        else:
            print("Записи не найдены.")
    elif choice == "5":
        modify_entry()
    elif choice == "6":
        delete_entry()
    elif choice == "7":
        print_phone_book()
    elif choice == "8":
        break
    else:
        print("Неверный пункт меню.")