# имя пользователя
family = input('Введите вашу фамилию: ')
name = input('Введите ваше имя: ')
otchestvo = input('Введите ваше очество: ')
print('Здравствуйте, ' + family + ' ' + name[:1] + '.' + otchestvo[:1] + '.')

# заголовок заметки
title = input('Введите название заметки: ')
print('Название заметки: ', title)

# описание заметки
content = input('Напишите подробнее о вашей заметке: ')
print('Описание заметки: ', content)

# статус заметки
status = input('Статус: ')
print('Статус заметки: ', status)

# дата создания заметки
created_date = input('Введите дату начала, ДД.ММ.ГГГГ: ')
print('Дата создания заметки: ', created_date[:6])

# дата истечения заметки (дедлайн)
issue_date = input('Введите дату окончания, ДД.ММ.ГГГГ: ')
print('Дата истечения заметки: ', issue_date[:6])