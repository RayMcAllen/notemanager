
print("Добро пожаловать в Менеджер заметок! Вы можете добавить новую заметку.")

# ЗАПРОС ИМЕНИ ПОЛЬЗОВАТЕЛЯ
name = input('Введите ваше имя:\n')

# СПИСОК
# ввод переменных
title_name = input("Введите название вашей заметки:\n")
titles = []

# создание цикла для переменной
while True:
    # запрос ввода от пользователя
    title = input('Введите ваш список (или нажмите "ENTER" или напишите "стоп" для завершения):\n')
    print(title, 'успешно добавлен в ваш список') #показываем пользователю, что команда выполнена

    # условие для завершения/продолжения цикла
    if title == '' or title == 'стоп':
        print("Список завершен") #показываем пользователю, что он закончил список
        break
    else:
        titles.append(title + '\n') #добавление элемента в конец списка

# убираем повторяющиеся элементы
unique_titles = list(set(titles))

# CТАТУС
# вводим значения переменных и отображаем их
status_1 = '1. Новая'
status_2 = '2. В процессе'
status_3 = '3. Выполнено'

# создаем словарь для использования его в функции
status = {'1': 'Новая', '2': 'В процессе', '3': 'Выполнено'}

# создаем функцию для изменения статуса заметки
def update_status():
    global status  # используем наш словарь
    while True:
        print('Возможные статусы заметки:\n', status_1, '\n', status_2, '\n', status_3) # подсказка для пользователя
        for i in status:
            i = input('Введите статус заметки (1,2 или 3): ') # запрашиваем ввод от пользователя
            if i == '1':
                status = {1: 'Новая'}
                print('Ваш выбор:', status_1)
                break
            elif i == '2':
                status = {2: 'В процессе'}
                print('Ваш выбор:', status_2)
                break
            elif i == '3':
                status = {3: 'Выполнено'}
                print('Ваш выбор:', status_3)
                break
            elif i != ('1', '2', '3'):  # предотвращаем ошибки в случае некорректного ввода пользователем
                print('Введено некорректное значение!')
            try:
                result = update_status()
                break
            except i != ('1', '2', '3'):
                print('Введено некорректное значение!')
                pass
        change_status = input('Желаете изменить статус заметки (y/n):\n') # уточняем, не желает ли пользователь изменить статус
        while change_status:
            if change_status == 'y':
                break
            elif change_status == 'n':
                return
            elif change_status != ('y', 'n'): # предотвращаем ошибки в случае некорректного ввода пользователя
                change_status = False
                print('Введено некорректное значение!')

# отображение результата
print('Статус заметки успешно обновлен!')


# ДЕДЛАЙН
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
        print("До завершения осталось ", remain.days, 'дней')
    elif remain.days < 1:
        print("Дедлайн завершился", -remain.days, "дней назад!")

#вызов созданных функций
update_status()
today()
issue_date()
deadline()

print("Имя:\n",name,"\n",
      'Название заметки: ', title_name,'\n',
      "Список:\n", unique_titles,
      "Статус:\n", status,'\n',
      "Дата создания:\n", datetime.datetime.today().strftime("%d.%m.%Y"),'\n', "Дата завершения:\n",
      create_date.strftime("%d.%m.%Y"))