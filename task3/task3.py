with open('1.txt', encoding='utf-8') as f1, open('2.txt', encoding='utf-8') as f2:
    # Создаем кортеж
    file1 = ('1.txt', f1.readlines())
    file2 = ('2.txt', f2.readlines())
    # Сравниваем
    if len(file1[1]) < len(file2[1]):
        first = file1
        second = file2
    else:
        first = file2
        second = file1
    # Итог
    result = f"{first[0]}\n{len(first[1])}\n{''.join(first[1])}"f"{second[0]}\n{len(second[1])}\n{''.join(second[1])}"

# Записываем и выводим
with open('result.txt', 'w', encoding='utf-8') as f:
    f.write(result)
    print(result)