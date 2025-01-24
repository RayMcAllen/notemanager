# Список словарей
data = [
    {"Имя": "Алексей", "Заголовок": "Список покупок", "Описание": "Купить продукты на неделю"},
    {"Имя": "Мария", "Заголовок": "Учеба", "Описание": "Подготовиться к экзамену"},
    {"Имя": "Петр", "Заголовок": "Первый", "Описание": "Она зовет меня Петр, ведь я у нее первый"}
]

# Распечатываем заметки с нумерацией
print("Текущие заметки:")
for i, item in enumerate(data, start=1):
    print(f"{i}. Имя: {item['Имя']}")
    print(f"   Заголовок: {item['Заголовок']}")
    print(f"   Описание: {item['Описание']}")

while True:
    # Запрос у пользователя
    find_note = input("Введите имя или заголовок заметки, которую хотите удалить: ")
    # Инициализируем индекс
    index = 0
    # Переменная для отслеживания найденного результата
    found = False
    # Используем цикл while для поиска словаря
    while index < len(data):
        if data[index]["Имя"].lower() == find_note.lower() or data[index]["Заголовок"].lower() == find_note.lower():
            print(f"Удалено: {data[index]}")
            found = True
            del data[index]
            break  # Выход из цикла, если нашли
        index += 1

    # Если не нашли имя
    if not found:
        print("Имя не найдено.")

    # Распечатываем заметки с нумерацией
    print("Текущие заметки:")
    for i, item in enumerate(data, start=1):
        print(f"{i}. Имя: {item['Имя']}")
        print(f"   Заголовок: {item['Заголовок']}")
        print(f"   Описание: {item['Описание']}")

    delete_another = input("Хотите удалить еще заметку? (да/нет): ")
    if delete_another.lower() != 'да':
        break


print("Текущие заметки:")
for i, item in enumerate(data, start=1):
    print(f"{i}. Имя: {item['Имя']}")
    print(f"   Заголовок: {item['Заголовок']}")
    print(f"   Описание: {item['Описание']}")

