# Задание №4
# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы
# функции.
import csv
import json


def func(source_file, dest_file):
    with (open(source_file, 'r') as f1,
          open(dest_file, 'w', encoding='utf-8') as file):
        csv_file = csv.reader(f1, delimiter=';')
        next(csv_file)
        new_dict = {}
        for level, pers_id, name in csv_file:
            pers_id = pers_id.rjust(10, '0')
            name = name.title()
            hash_id = hash(name + pers_id)
            new_dict[hash_id] = {pers_id: [name, level]}
        json.dump(new_dict, file, indent=2)


