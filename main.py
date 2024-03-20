# Zad#1
import csv

def create_dict_from_file(file_dir, file_name):
    """Функция чтения файла + создание словаря нужного формата"""
    file_path = os.path.abspath(os.path.join(file_dir, file_name))
    cook_dict = {}
    with open(file_path, encoding='utf8') as file_work:
        for line in file_work:
            dish_name = line.lower().strip()
            counter = int(file_work.readline())
            list_of_ingridient = []
            for i in range(counter):
                temp_dict = {}
                ingridient = file_work.readline().lower()
                ingridient = ingridient.strip().split('|')
                temp_dict['ingridient_name'] = ingridient[0].strip()
                temp_dict['quantity'] = int(ingridient[1])
                temp_dict['measure'] = ingridient[2].strip()
                list_of_ingridient.append(temp_dict)
            cook_dict[dish_name] = list_of_ingridient
            file_work.readline()
    return cook_dict

cook_book = read_cook_book('recipes.csv')
print(cook_book)

#Zad#2
def get_shop_list_by_dishes(dishes, person_count):
  """
  Возвращает словарь с названиями ингредиентов и их количествами для заданных блюд и количества персон.
  """
  shop_list = {}
  for dish in dishes:
    for ingredient in cook_book[dish]:
      ingredient_name = ingredient['ingredient_name']
      quantity = ingredient['quantity'] * person_count
      measure = ingredient['measure']
      if ingredient_name in shop_list:
        shop_list[ingredient_name]['quantity'] += quantity
      else:
        shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}
  return shop_list

shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print(shop_list)

