import json


def check_capacity(max_capacity: int, guests: list) -> bool:
    datas = []
    occupied_rooms = 0
    for guest in guests:
        datas.append((guest['check-in'],1))
        datas.append((guest['check-out'],-1))
    for data, status in sorted(datas):
        occupied_rooms += status
        if occupied_rooms > max_capacity:
            return False
    return True


if __name__ == "__main__":
    # Чтение входных данных
    # Первая строка - вместимость гостиницы
    max_capacity = int(input())
    # Вторая строка - количество записей о гостях
    n = int(input())

    guests = []
    # Читаем n строк, json-данные о посещении.
    for _ in range(n):
        guest = json.loads(input())
        guests.append(guest)

    # Вызов функции
    result = check_capacity(max_capacity, guests)
    # Вывод результата
    print(result)