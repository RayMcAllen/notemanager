def display_notes(notes):
    if not notes:
        print("У вас нет сохранённых заметок.")
        return

    print("Список заметок:")
    print("------------------------------")

    for index, note in enumerate(notes, start=1):
        print(f"Заметка №{index}:")
        print(f"Имя пользователя: {note.get('username', 'Не указано')}")
        print(f"Заголовок: {note.get('title', 'Не указан')}")
        print(f"Описание: {note.get('description', 'Не указано')}")
        print(f"Статус: {note.get('status', 'Не указан')}")
        print(f"Дата создания: {note.get('created_date', 'Не указана')}")
        print(f"Дедлайн: {note.get('deadline', 'Не указан')}")
        print("------------------------------")


# Пример использования функции:
notes_example = [
    {
        'username': 'Алексей',
        'title': 'Список покупок',
        'description': 'Купить продукты на неделю',
        'status': 'новая',
        'created_date': '27.11.2024',
        'deadline': '30.11.2024'
    },
    {
        'username': 'Мария',
        'title': 'Учеба',
        'description': 'Подготовиться к экзамену',
        'status': 'в процессе',
        'created_date': '25.11.2024',
        'deadline': '01.12.2024'
    }
]

# Вызов функции с примерами
display_notes(notes_example)
display_notes([])  # Тест для пустого списка
