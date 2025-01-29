

notes = []

def create_note():
    while True:
        print("Добро пожаловать в Менеджер заметок! Вы можете добавить новую заметку.")
        # ЗАПРОС ИМЕНИ ПОЛЬЗОВАТЕЛЯ
        name = input('Введите ваше имя: ')
        # СПИСОК
        title = input('Введите название заметки: ')
        content = []
        # создание цикла для переменной
        while True:
            # запрос ввода от пользователя
            add_content = input('Введите ваш список (или нажмите "ENTER" или напишите "стоп" для завершения): ')
            # условие для завершения/продолжения цикла
            if add_content == '' or add_content == 'стоп':
                print("Список завершен")  # показываем пользователю, что он закончил список
                break
            else:
                content.append(add_content)  # добавление элемента в конец списка
                print(add_content, 'успешно добавлен в ваш список')  # показываем пользователю, что команда выполнена
            # убираем повторяющиеся элементы
            unique_titles = list(set(content))
            # вывод строки для красоты
            print('Ваш список: ')
            # вывод итогового списка столбиком
            print(', '.join(unique_titles))

        # CТАТУС ЗАМЕТКИ
        print('Возможные статусы заметки:\n', '1. Выполнено', '\n', '2. В процессе', '\n',
              '3. Отложено')  # подсказка для пользователя
        while True:
            status = input('Введите статус заметки (1, 2 или 3): ')
            if status == '1':
                status = '1. Выполнено'
                print('Ваш выбор: 1. Выполнено')
                break
            elif status == '2':
                status = '2. В процессе'
                print('Ваш выбор: 2. В процессе')
                break
            elif status == '3':
                status = '3. Отложено'
                print('Ваш выбор: 3. Отложено')
                break
            else:
                print('Введено некорректное значение!')

        # ДЕДЛАЙН
        import datetime  # импортируем библиотеку для работы с датами
        print("Сегодня: ", datetime.datetime.now().strftime("%d.%m.%Y"))
        while True:
            # Запрос даты у пользователя
            create_date = input('Введите дату завершения дед лайна в формате ДД.ММ.ГГГГ: ')

            # проверка корректности ввода даты
            try:
                create_date = datetime.datetime.strptime(create_date, "%d.%m.%Y")
            except ValueError:
                print("Дата введена некорректно!")
                continue

            # Вывод отформатированной даты
            print('Дата завершения дед лайна:\n', create_date.strftime("%d.%m.%Y"))

            # Вычисление оставшегося времени
            remain = create_date - datetime.datetime.now()

            # Проверка оставшегося времени
            if remain.days > 0:
                print("Осталось", remain.days, 'дней')
                break
            elif remain.days < 0:
                print("Дедлайн завершен", -remain.days, "дней назад")
                break
            else:
                print("Дедлайн сегодня")
                break

        note = {'username': name, 'title': title,
                'content': content, 'status': status,
                'created_date': datetime.datetime.now().strftime("%d.%m.%Y"),
                'issue_date': create_date.strftime("%d.%m.%Y")}

        notes.append(note)

        print("Заметка успешно добавлена!")
        for i, item in enumerate(notes, start=1):
            print(f"{i}. Имя пользователя: {item['username']}")
            print(f"   Заголовок заметки: {item['title']}")
            print(f"   Описание заметки: {item['content']}")
            print(f"   Статус заметки: {item['status']}")
            print(f"   Дата создания заметки: {item['created_date']}")
            print(f"   Дата истечения заметки: {item['issue_date']}")

        another_note = input('Желаете добавить еще заметку? (y/n): ')
        while another_note:
            if another_note == 'y':
                break
            elif another_note == 'n':
                return main()
            else:
                print("Введено некорректное значение!")

def display_notes():
    if not notes:
        print("У вас нет сохранённых заметок.")
        return

    print("Список заметок:")
    print("------------------------------")

    for index, note in enumerate(notes, start=1):
        print(f"Заметка №{index}:")
        print(f"Имя пользователя: {note.get('username', 'Не указано')}")
        print(f"Заголовок: {note.get('title', 'Не указан')}")
        print(f"Описание: {note.get('content', 'Не указано')}")
        print(f"Статус: {note.get('status', 'Не указан')}")
        print(f"Дата создания: {note.get('created_date', 'Не указана')}")
        print(f"Дедлайн: {note.get('issue_date', 'Не указан')}")
        print("------------------------------")

from datetime import datetime
# Функция для проверки корректности даты
def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%d.%m.%Y")
        return True
    except ValueError:
        return False

def update_note(note):
    print("Текущие данные заметки:", note)
    # Вводим ключи заметки
    keys = ['username', 'title', 'content', 'status', 'issue_date']

    while True:
        # Запрос выбора ключа для обновления
        key = input(f"Какие данные вы хотите обновить? ({', '.join(keys)}): ")

        if key not in keys:
            print("Некорректное имя поля. Пожалуйста, выберите одно из следующих: ", ', '.join(keys))
            continue

        # Запрос нового значения
        if key == 'issue_date':
            while True:
                new_value = input(f"Введите новое значение для {key} (формат: ДД.ММ.ГГГГ): ")
                if is_valid_date(new_value):
                    break
                else:
                    print("Некорректный формат даты. Попробуйте снова.")
        else:
            new_value = input(f"Введите новое значение для {key}: ")

        # Обновление заметки
        note[key] = new_value
        print("Заметка обновлена:", note)
        break

    return note


def delete_note():
    while True:
        # Запрос у пользователя
        find_note = input("Введите имя или заголовок заметки, которую хотите удалить: ")
        # Инициализируем индекс
        index = 0
        # Переменная для отслеживания найденного результата
        found = False
        # Используем цикл while для поиска словаря
        while index < len(notes):
            if notes[index]["username"].lower() == find_note.lower() or notes[index]["title"].lower() == find_note.lower():
                print(f"Удалено: {notes[index]}")
                found = True
                del notes[index]
                break  # Выход из цикла, если нашли
            index += 1
        # Если не нашли имя или заголовок
        if not found:
            print("Имя или заголовок не найдены.")

        delete_another = input("Хотите удалить еще заметку? (да/нет): ")
        if delete_another.lower() != 'да':
            break


def show_menu():
    print("Доступные действия:")
    print("1: Создать новую заметку")
    print("2: Показать все заметки")
    print("3: Обновить заметку")
    print("4: Удалить заметку")
    print("5: Найти заметки")
    print("6: Выйти из программы")

def search_notes(notes, keyword=None, status=None):
    # Обработка пустого списка заметок
    if not notes:
        print("Нет доступных заметок.")
        return
    # Поиск заметок с учетом keyword и status
    filtered_notes = []
    for note in notes:
        matches_keyword = True
        matches_status = True

        if keyword:
            # Проверка на наличие ключевого слова в полях title, content, or username
            matches_keyword = (keyword.lower() in note['title'].lower() or
                               keyword.lower() in note['content'].lower() or
                               keyword.lower() in note['username'].lower())

        if status:
            # Проверка на совпадение со статусом
            matches_status = (note['status'].lower() == status.lower())

        if matches_keyword and matches_status:
            filtered_notes.append(note)
        elif matches_keyword and status is None:
            filtered_notes.append(note)
        elif matches_status and keyword is None:
            filtered_notes.append(note)

    # Вывод результатов
    if filtered_notes:
        print("Найдены заметки:")
        for i, note in enumerate(filtered_notes, start=1):
            print(f"Заметка №{i}:")
            print(f"Имя пользователя: {note['username']}")
            print(f"Заголовок: {note['title']}")
            print(f"Описание: {note['content']}")
            print(f"Статус: {note['status']}\n")
    else:
        print("Заметки, соответствующие запросу, не найдены.")

def main():
    while True:
        show_menu()
        choice = input("Выберите действие (1-6): ")

        if choice == '1':
            create_note()
        elif choice == '2':
            display_notes()
        elif choice == '3':
            if not notes:
                print("Нет заметок для обновления.")
            else:
                display_notes()
                note_index = int(input("Введите номер заметки для обновления: ")) - 1
                if 0 <= note_index < len(notes):
                    notes[note_index] = update_note(notes[note_index])
                else:
                    print("Некорректный номер заметки.")
        elif choice == '4':
            delete_note()
        elif choice == '5':
            search_notes(notes, keyword=input('Введите ключевое слово (или нажмите ENTER, чтобы пропустить): '),
                         status=input("Введите статус заметки (или нажмите ENTER, чтобы пропустить): "))
        elif choice == '6':
            print("Выход из программы.")
            exit(0)
        else:
            print("Ошибка: недопустимый номер действия. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()