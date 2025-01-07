import datetime #импортируем библиотеку для работы с датами

# функция для определения текущей даты
def today():
    date = datetime.datetime.today().strftime("%d.%m.%Y")
    print("Сегодня:\n", date)

# функция для обработки пользовательского ввода
def issue_date():
    while True:
        global create_date
        create_date = input('Введите дату завершения дедлайна в формате ДД.ММ.ГГГГ:\n')
        try:
            create_date = datetime.datetime.strptime(create_date, "%d.%m.%Y")
        except:
            print("Дата введена некорректно!")
            continue
        print('Дата завершения дедлайна:\n', create_date.strftime("%d.%m.%Y"))
        return

# функция для расчета разницы между датами
def deadline():
    remain = create_date - datetime.datetime.now()
    if remain.days > 1:
        print("Осталось ", remain.days, 'дней')
    elif remain.days < 1:
        print("Дедлайн завершился", -remain.days, "дней назад!")

#вызов созданных функций
today()
issue_date()
deadline()