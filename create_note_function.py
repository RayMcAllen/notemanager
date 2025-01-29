
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
                exit()
            else:
                print("Введено некорректное значение!")

create_note()
