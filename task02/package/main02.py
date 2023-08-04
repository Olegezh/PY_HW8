# Задание №2
# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.
import json


def json_list():
    while True:
        str_inp = input('Введите данные: ')
        if str_inp:
            name, pers_id, level = str_inp.split()
            level = int(level)
            if not 0 < int(level) < 8:
                print('Давай сначала')
                continue
            with open('my_file.json', 'r') as f:
                try:
                    data = json.load(f)
                except:
                    data = {}
            if level not in data:
                data[level] = {}
            data[level][pers_id] = name
            with open('my_file.json', 'w') as f:
                json.dump(data, f, indent=2)
        else:
            break
