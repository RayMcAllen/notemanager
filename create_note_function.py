import datetime  # импортируем библиотеку для работы с датами

data = []

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
        status = input('Введите статус заметки (1,2 или 3): ')
        while status:
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
            else:  # предотвращаем ошибки в случае некорректного ввода пользователем
                print('Введено некорректное значение!')

        # ДЕДЛАЙН
        print("Сегодня: ", datetime.datetime.now().strftime("%d.%m.%Y"))
        while True:
            # Запрос даты у пользователя
            create_date = input('Введите дату завершения дедлайна в формате ДД.ММ.ГГГГ: ')

            # проверка корректности ввода даты
            try:
                create_date = datetime.datetime.strptime(create_date, "%d.%m.%Y")
            except ValueError:
                print("Дата введена некорректно!")
                continue

            # Вывод отформатированной даты
            print('Дата завершения дедлайна:\n', create_date.strftime("%d.%m.%Y"))

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

        note = {'Имя пользователя': name, 'Заголовок заметки': title,
                'Описание заметки': content, 'Статус заметки': status,
                'Дата создания заметки': datetime.datetime.now().strftime("%d.%m.%Y"),
                'Дата истечения заметки': create_date.strftime("%d.%m.%Y")}

        data.append(note)

        for i, item in enumerate(data, start=1):
            print(f"{i}. Имя пользователя: {item['Имя пользователя']}")
            print(f"   Заголовок заметки: {item['Заголовок заметки']}")
            print(f"   Описание заметки: {item['Описание заметки']}")
            print(f"   Статус заметки: {item['Статус заметки']}")
            print(f"   Дата создания заметки: {item['Дата создания заметки']}")
            print(f"   Дата истечения заметки: {item['Дата истечения заметки']}")

        another_note = input('Желатете добавить еще заметку? (y/n): ')
        while another_note:
            if another_note == 'y':
                break
            elif another_note == 'n':
                exit(0)
            else:
                print("Введено некорректное значение!")

create_note()
