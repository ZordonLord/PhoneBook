# Телефонная книга с GUI на tkinter
# Функции:
# 1. Импортировать данные из файла
# 2. Экспортировать данные в файл
# 3. Добавить запись
# 4. Поиск по фамилии или имени
# 5. Изменить запись
# 6. Удалить запись
# 7. Вывести все записи

from tkinter import *

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
    new_window_add = Toplevel(root)
    new_window_add.title = "Введите Фамилию:"
    last_name = entry_text
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


root = Tk()
root.title('Телефонная книга')
root.geometry('600x600')

phone_book = {}

btn1 = Button(root,
             text = '1. Импортировать данные из файла',
             command= 'import_data',
             font = 'Arial 20',
             bg = 'lime',
             activebackground = 'blue',
             width='30'
             )

btn2 = Button(root,
             text = '2. Экспортировать данные в файл',
             command= 'export_data',
             font = 'Arial 20',
             bg = 'lime',
             activebackground = 'blue',
             width='30'
             )

btn3 = Button(root,
             text = '3. Добавить запись',
             command = 'add_person',
             font = 'Arial 20',
             bg = 'lime',
             activebackground = 'blue',
             width='30'
             )

btn4 = Button(root,
             text = '4. Поиск по фамилии или имени',
             command= '',
             font = 'Arial 20',
             bg = 'lime',
             activebackground = 'blue',
             width='30'
             )

btn5 = Button(root,
             text = '5. Изменить запись',
             command= '',
             font = 'Arial 20',
             bg = 'lime',
             activebackground = 'blue',
             width='30'
             )

btn6 = Button(root,
             text = '6. Удалить запись',
             command= '',
             font = 'Arial 20',
             bg = 'lime',
             activebackground = 'blue',
             width='30'
             )

btn7 = Button(root,
             text = '7. Вывести все записи',
             command= 'print_phone_book',
             font = 'Arial 20',
             bg = 'lime',
             activebackground = 'blue',
             width='30'
             )

btn8 = Button(root,
             text = '8. Выход',
             command= 'exit',
             font = 'Arial 20',
             bg = 'lime',
             activebackground = 'blue',
             width='30'
             )

label_text = Label(root, text ='Выберите пункт меню: ', font = "Arial 20")

label_input = Label(root, text ='', font = "Arial 20")

entry_text = Entry(root,
                   font = 'Arial 20')


label_text.pack()
label_input.pack()
btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
btn5.pack()
btn6.pack()
btn7.pack()
btn8.pack()

root.mainloop()