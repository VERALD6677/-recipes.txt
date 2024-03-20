#Zad#3
import os

file_contents = {}

# Читаем содержимое файлов и сохраняем количество строк
for filename in os.listdir('.'):
    if filename.endswith('.txt'):
        with open(filename, 'r') as file:
            lines = file.readlines()
            file_contents[filename] = {
                'num_lines': len(lines),
                'content': lines
            }

# Сортируем файлы по количеству строк
sorted_files = sorted(file_contents.items(), key=lambda x: x[1]['num_lines'])

# Записываем отсортированное содержимое в новый файл
with open('result.txt', 'w') as result_file:
    for file_name, content in sorted_files:
        result_file.write(f"{file_name}\n{content['num_lines']}\n")
        result_file.writelines(content['content'])
        result_file.write('\n\n')

print("Готово! 'result.txt'")
