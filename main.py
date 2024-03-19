# Zad#1
import csv

def read_cook_book(file_name):
  """
  Читает файл с рецептами и возвращает словарь, где ключами являются названия блюд,
  а значениями - списки словарей с ингредиентами.
  """
  cook_book = {}
  with open(file_name, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
      dish_name = row[0]
      num_ingredients = int(row[1])
      ingredients = []
      for i in range(2, num_ingredients * 3 + 2, 3):
        ingredient_name = row[i]
        quantity = int(row[i + 1])
        measure = row[i + 2]
        ingredients.append({
          'ingredient_name': ingredient_name,
          'quantity': quantity,
          'measure': measure
        })
      cook_book[dish_name] = ingredients
  return cook_book

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

