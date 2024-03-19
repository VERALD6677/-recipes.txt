#Zad#3
import os

def merge_files(files):
  """
  Объединяет несколько файлов в один по правилам, описанным в задаче.
  """
  result_file = open('merged_files.txt', 'w')
  for file in files:
    with open(file, 'r') as f:
      num_lines = len(f.readlines())
    result_file.write(f'{file}\n{num_lines}\n')
    with open(file, 'r') as f:
      result_file.write(f.read())
    result_file.write('\n')
  result_file.close()

files = ['1.txt', '2.txt', '3.txt']
merge_files(files)
