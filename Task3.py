Dict_RusToEng = {'Программирование': 'Programming', 'Это': 'Is', 'Круто': 'Cool'}  # Русско-английский словарь
Dict_EngToRus = {'Programming': 'Программирование', 'Is': 'Это', 'Cool': 'Круто'}  # Английско-русский словарь

while True:
    print("С какого языка вы хотите перевести? рус/англ")
    lang = input()
    if lang == 'рус':  # выбор русского языка
        print("Введите строку на русском")
        rus = input().split(' ')
        rus = [x.capitalize() for x in
               rus]  # Каждое введённое слово начинается с заглавной буквы, а остальные с нижним регистром
        RusToEng = [Dict_RusToEng.get(x.capitalize()) if Dict_RusToEng.get(x) else x for x in rus]
        print(*RusToEng)
        break

    if lang == 'англ':  # Выбор английского языка
        print("Введите строку на английском")
        eng = input().split(' ')
        eng = [x.capitalize() for x in
               eng]  # Каждое введённое слово начинается с заглавной буквы, а остальные с нижним регистром
        EngToRus = [Dict_EngToRus.get(x.capitalize()) if Dict_EngToRus.get(x) else x for x in eng]
        print(*EngToRus)
        break
    else:
        print("Попробуйте снова, вы ввели неверную команду")
