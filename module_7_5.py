import os
import time

directory = "."

for root, dirs, files in os.walk(directory):
    # print(root, dirs, files)
    if '.venv' in root or '.idea' in root:
        continue

    for file in files:
        file_path = os.path.join(root, file)
        file_time = time.strftime("%Y.%m.%d %H:%M", time.gmtime(os.path.getmtime(file_path)))
        file_size = os.path.getsize(file_path)
        parent_dir = root
        print(f'Обнаружен файл: {file}, Путь: {file_path}, Размер: {file_size} байт, Время изменения: {file_time}, Родительская директория: {parent_dir}')

