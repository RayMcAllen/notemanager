import datetime

# Функция для определения текущей даты
def get_current_date():
    return datetime.datetime.now().strftime("%d.%m.%Y")

# Функция для обработки пользовательского ввода
def issue_date():
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

# Вызов функций
print("Сегодня:", get_current_date())
issue_date()
