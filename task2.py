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

#print(cook_book['Омлет'])
#print(cook_book['Утка по-пекински'])
#print(cook_book['Запеченный картофель'])
#print(cook_book['Фахитос'])
#print(cook_book)
def get_shop_list_by_dishes(dishes: list, person_count: int):
    total = {} # словарь с названием ингредиентов и его количества для блюда
    for dish in dishes:
        if dish in cook_book:
            for ingredients in cook_book[dish]:
                #print(ingredients)
                if ingredients['ingredient_name'] in total:
                    total[ingredients['ingredient_name']]['quantity'] += int(ingredients['quantity']) * person_count
                else:
                    total[ingredients['ingredient_name']] = {'measure': ingredients['measure'],'quantity': (int(ingredients['quantity']) * person_count)}
        else:
            print(f'Блюда "{dish}" нет в книге рецептов')

    #print(total)
    pprint.pprint(dict(sorted(total.items())))


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
#get_shop_list_by_dishes(['Фахитос', 'Омлет'], 1)
#get_shop_list_by_dishes(['Борщ', 'Утка по-пекински'], 1)