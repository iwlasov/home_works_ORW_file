
import os

in_files = ['1.txt', '2.txt', '3.txt']
out_file = '4.txt'
files = []

def str_count(file:str) -> int: # функция подсчета строк в файле
    with open(file, 'rt', encoding='utf-8') as f:
        counting = 0
        for line in f.readlines():
            counting += 1
    return counting

for name in in_files:
    files.append([str_count(name), name]) #список файлов и колва строк в них

#print(files)
if os.path.exists(out_file): #пересоздаем файл результата
    os.remove(out_file)

for in_file in sorted(files): # цикл по файлам
        open_file = open(out_file, 'a')
        open_file.write(f'{in_file[1]}\n') # имя файла и
        open_file.write(f'{in_file[0]}\n') #  количество строк в нем
        with open(in_file[1], 'r',encoding='utf-8') as file:
            count = 1
            for line in file: # заполняем построчно результирующий файл
                open_file.write(f'строка номер {count} файла номер {in_file[1][0]} {line}')
                count += 1
        open_file.write(f'\n')
        open_file.close()
