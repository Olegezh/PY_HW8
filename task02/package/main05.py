# Задание №5
# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов
import json
import os
import pickle


def rename_file():
    for file in os.listdir():
        if file.endswith('.json'):
            with (open(file, 'r') as file_inp,
                  open(f'{file[:-5]}.pickle', 'wb') as file_out):
                pickle.dump((json.load(file_inp)), file_out)

