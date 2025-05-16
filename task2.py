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

# # Наводим красоту
# print('cook_book = {')
# for dish, ingredients in cook_book.items():
#     print(f"  '{dish}': [")
#     for ing in ingredients:
#         print(f"    {{'ingredient_name': '{ing['ingredient_name']}', 'quantity': {ing['quantity']}, 'measure': '{ing['measure']}'}},")
#     print('  ],')
# print('}')


def get_shop_list_by_dishes(dishes, person_count, cook_book):
    # Список блюд и количества персон
    shop_list = {}

    for dish in dishes:

        for ingredient in cook_book[dish]:
            name = ingredient['ingredient_name']
            measure = ingredient['measure']
            quantity = ingredient['quantity'] * person_count

            if name in shop_list:
                shop_list[name]['quantity'] += quantity
            else:
                shop_list[name] = {
                    'measure': measure,
                    'quantity': quantity
                }

    return shop_list


def main():
    # Загружаем рецепты
    cook_book = read_recipes('recipes.txt')

    # Выводим список доступных блюд
    available_dishes = list(cook_book.keys())
    print("\nДоступные блюда:")
    for i, dish in enumerate(available_dishes, 1):
        print(f"{i}. {dish}")

    # Запрашиваем нужные блюда у пользователя
    selected_dishes = []
    while True:
        number_dish = input("\nВведите номер блюда (или '0 для завершения): ").strip().lower()
        if number_dish == '0':
            break

        if not number_dish.isdigit():
            print("Пожалуйста, введите номер блюда")
            continue

        dish_index = int(number_dish) - 1
        if 0 <= dish_index < len(available_dishes):
            selected_dishes.append(available_dishes[dish_index])
            print(f"Добавлено: {available_dishes[dish_index]}")
        else:
            print("Нет блюда с таким номером")

    if not selected_dishes:
        print("Не выбрано ни одного блюда")
        return

    # Запрашиваем количество персон
    number_person = 0
    while number_person <= 0:
        persons_input = input("\nНа сколько персон готовим? ").strip()
        if persons_input.isdigit() and int(persons_input) > 0:
            number_person = int(persons_input)
        else:
            print("Введите положительное число")

    # Выводим список покупок
    shopping_list = get_shop_list_by_dishes(selected_dishes, number_person, cook_book)

    print(f"\nСписок ингредиентов для {number_person} персон:")
    print(f"Выбранные блюда: {', '.join(selected_dishes)}")
    print("{")
    for item, details in shopping_list.items():
        print(f"  '{item}': {{'measure': '{details['measure']}', 'quantity': {details['quantity']}}},")
    print("}")

1
if __name__ == '__main__':
    main()