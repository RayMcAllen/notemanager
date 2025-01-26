def search_notes(data, keyword=None, status=None):
    # Обработка пустого списка заметок
    if not data:
        print("Нет доступных заметок.")
        return

    # Поиск заметок с учетом keyword и status
    filtered_notes = []
    for note in data:
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


# Пример использования
data = [
    {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status': 'новая',
     'created_date': '27.11.2024', 'issue_date': '30.11.2024'},
    {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену', 'status': 'в процессе',
     'created_date': '25.11.2024', 'issue_date': '01.12.2024'},
    {'username': 'Иван', 'title': 'План работы', 'content': 'Завершить проект', 'status': 'выполнено',
     'created_date': '20.11.2024', 'issue_date': '26.11.2024'}
]

# Примеры вызова функции
search_notes(data, keyword='покупок')
search_notes(data, status='в процессе')
search_notes(data, keyword='работы', status='выполнено')

while True:
    search_notes(data, keyword=input('Введите ключевое слово (или нажмите ENTER, чтобы пропустить): '),
                 status=input("Введите статус заметки (или нажмите ENTER, чтобы пропустить): "))