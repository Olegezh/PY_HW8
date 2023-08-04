# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.

import json
import os
import csv
import pickle


def scan_folders(path, data, folder_size = 0):
    folder_size = 0
    for i in os.listdir(path):
        if os.path.isdir(path+'\\'+i):
            marker = "folder"
            scan_folders(path+'\\'+i, data)
            file_size = "no idea"
            # file_size = folder_size
        else:
            marker = "file"
            file_size = os.path.getsize(path+'\\'+i)

        # folder_size += file_size
        str_path = path+"\\"+i
        data[str_path] = [marker, file_size]

    # return folder_size

data = {}
path = input('ввежите путь к папке: ')
# _ = scan_folders(path, data)
scan_folders(path, data)
# print(*data.items(), sep="\n")

with open('list.json', 'w') as f:
    json.dump(data, f, indent=2)

with open('list.csv', 'w', encoding='utf-8', newline='') as f:
    columns = ['path', 'title', 'size']
    writer = csv.writer(f, delimiter=';')
    writer.writerow(columns)
    result = []
    for key, value in data.items():
        result.append([key, value[0], value[1]])
        writer.writerows(result)

with open('list.picle', 'wb') as f:
    pickle.dump(data, f)
