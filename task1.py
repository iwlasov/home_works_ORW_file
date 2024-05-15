import pprint

cook_book = {} # словарь блюд

with open('recipes.txt', encoding='utf-8') as file:
    for dishes in file: # цикл по блюдам в файле
        #print(dishes)
        dish = dishes.strip() # ключ словаря - название блюда
        #print(dish)
        ingredients_count = file.readline().strip()
        #print(ingredients_count)
        ingredients = [] # список ингредиентов блюда

        for ingredient in range(int(ingredients_count)): # цикл по ингредиентам в блюде
            recipe = file.readline().strip().split(' | ')
            #print(recipe)
            ingredient_name, quantity, measure = recipe
            ingredients.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})

        file.readline() # читаем пустую строку между рецептами
        cook_book[dish] = ingredients

pprint.pprint(cook_book)
