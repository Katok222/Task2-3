import os

# Список файлов для объединения
file_list = [
   "C:/Users/DNS/Desktop/Задание 3/1.txt",
    "C:/Users/DNS/Desktop/Задание 3/2.txt",
    "C:/Users/DNS/Desktop/Задание 3/3.txt"
]

# Словарь для хранения содержимого и количества строк файлов
file_data = {}

# Чтение файлов и подсчет строк
for file in file_list:
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        file_data[file] = (len(lines), lines)

# Сортировка файлов по количеству строк
sorted_files = sorted(file_data.items(), key=lambda x: x[1][0])

# Запись в результующий файл
with open('C:/Users/DNS/Desktop/Задание 3/result.txt', 'w', encoding='utf-8') as result_file:
    for file_name, (line_count, lines) in sorted_files:
        result_file.write(f"{file_name}\n")  # Имя файла
        result_file.write(f"{line_count}\n")  # Количество строк
        result_file.writelines(lines)  # Содержимое файла