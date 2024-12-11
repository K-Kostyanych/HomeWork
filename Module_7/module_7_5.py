import time
import os

directory = os.getcwd()# Проход по всем файлам и папкам в указанной директории

print('Текущая директория: ', directory)

for root, dirs, files in os.walk(directory):
    # Функция os.walk() позволяет рекурсивно обходить все файлы и папки в указанной директории. Она возвращает кортеж из трех элементов
  for file in files:
      file_path = os.path.join(root, file)
      print(file_path)
      file_time = os.path.getmtime(file_path) # преобразует время из формата UNIX в локальное время.
      print(file_time)
      formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(file_time))# форматирует дату в привычный вид "день.месяц.год часы:минуты".
      print(formatted_time)
      file_size = os.path.getsize(file_path) # возвращает размер файла в байтах.
      print(file_size)
      parent_dir = os.path.dirname(file_path)

print(f'Обнаружен файл: {file}, Путь: {file_path}, Размер: {file_size} байт, Время изменения: {formatted_time},'
          f' Родительская директория: {parent_dir}')
