import csv
import sys

def search_stamp_by_number(number):
    """Поиск штампа по номеру"""
    try:
        with open('data/stamps.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Номер'] == str(number):
                    return row
        return None
    except FileNotFoundError:
        print("Файл данных не найден!")
        return None

def display_stamp(stamp_data):
    """Отображение штампа в нужном формате"""
    if stamp_data:
        print(f"# Штамп {stamp_data['Номер']}\n")
        print(f"| Место | {stamp_data['Место']} |")
        print(f"| 23    | {'':<15} |\n")
        print("Рабочее давление")
        print(f"{stamp_data['Рабочее_давление']}\n")
        print("Матрица")
        print(f"{stamp_data['Матрица']}\n")
        print("Комментарии")
        print(f"{stamp_data['Комментарии']}")
    else:
        print("Штамп не найден")

if name == "main":
    if len(sys.argv) > 1:
        number = sys.argv[1]
        stamp = search_stamp_by_number(number)
        display_stamp(stamp)
    else:
        print("Использование: python search.py <номер_штампа>")
        print("Пример: python search.py 20245")
