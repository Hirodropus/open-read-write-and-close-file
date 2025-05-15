def read_recipes(file):
    cook_book = {}
    with open(file, 'r', encoding='utf-8') as f:
        while True:
            # Блюдо
            dish_name = f.readline().strip()
            if not dish_name:
                break
            # Ингредиенты
            ingredient_count = int(f.readline().strip())
            ingredients = []
            # Читаем ингредиент
            for _ in range(ingredient_count):
                ingredient_line = f.readline().strip()
                # Пропускаем пустые строки
                if not ingredient_line:
                    continue
                # Разбираем строку с ингредиентом
                name, quantity, measure = map(str.strip, ingredient_line.split('|'))
                # Создаем словарь ингредиента
                ingredients.append({'ingredient_name': name,'quantity': int(quantity),'measure': measure})
            cook_book[dish_name] = ingredients
            # Пропускаем пустую строку между рецептами
            f.readline()

    return cook_book

cook_book = read_recipes('recipes.txt')

# Наводим красоту
print('cook_book = {')
for dish, ingredients in cook_book.items():
    print(f"  '{dish}': [")
    for ing in ingredients:
        print(f"    {{'ingredient_name': '{ing['ingredient_name']}', 'quantity': {ing['quantity']}, 'measure': '{ing['measure']}'}},")
    print('  ],')
print('}')
