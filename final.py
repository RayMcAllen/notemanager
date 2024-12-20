
# имя пользователя
family = input('Введите вашу фамилию: ')
name = input('Введите ваше имя: ')
otchestvo = input('Введите ваше очество: ')
username = [family, name, otchestvo]
print('Здравствуйте, ', + family + ' ' + name[:1] + '.' + otchestvo[:1] + '.')
# заголовок заметки
title = input('Введите основное название заметки: ')
title1 = input('Введите доп. название заметки: ')
title2 = input('Введите доп. название заметки: ')
alltitle = [title, title1, title2]
print(alltitle)

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

# словарь
note = {'Имя пользователя':username,'Заголовок заметки':alltitle, 'Описание заметки':content, 'Статус заметки':status, 'Дата создания заметки':created_date, 'Дата истечения заметки':issue_date}
print(note)