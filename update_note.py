from datetime import datetime

# Функция для проверки корректности даты
def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%d.%m.%Y")
        return True
    except ValueError:
        return False

# Функция изменения статуса
def update_note(note):
    print("Текущие данные заметки:", note)
    # Вводим ключи заметки
    keys = ['Имя', 'Заголовок', 'Описание', 'Статус', 'Дата истечения']

    while True:
        # Запрос выбора ключа для обновления
        key = input(f"Какие данные вы хотите обновить? ({', '.join(keys)}): ")

        if key not in keys:
            print("Некорректное имя поля. Пожалуйста, выберите одно из следующих: ", ', '.join(keys))
            continue

 
        # Запрос нового значения
        if key == 'Дата истечения':
            while True:
                new_value = input(f"Введите новое значение для {key} (формат: ДД.ММ.ГГГГ): ")
                if is_valid_date(new_value):
                    break
                else:
                    print("Некорректный формат даты. Попробуйте снова.")
        else:
            new_value = input(f"Введите новое значение для {key}: ")

        # Обновление заметки
        note[key] = new_value
        print("Заметка обновлена:", note)
        break

    return note


# Использование функции
if __name__ == "__main__":
    # Пример заметки
    note_example = {
        'Имя': 'Алексей',
        'Заголовок': 'Список покупок',
        'Описание': 'Купить продукты на неделю',
        'Статус': 'Новая',
        'Дата создания': '27.11.2024',
        'Дата истечения': '30.11.2024'
    }

    updated_note = update_note(note_example)
