authors = {'Клайв С. Льюис': ['Хроники Нарнии', 'Письма Баламута'],
           'В.А. Бондаренко': ['Математический анализ. Тексты лекций',
                               'Методические материалы для подготовки к экзамену'],
           'Артур Кларк': ['Космическая Одиссея']}


def books_by_author():
    while True:
        print("Выберите автора ", list(authors.keys()))

        author = input()
        if authors.get(author) == 0:
            print("Такого автора нет в списке, попробуйте снова.")
        if authors.get(author):
            print(authors[author])
            break


def author_by_books(bks):
    print("Введтие произведение")
    book = input().split(',')
    authors[bks].extend(map(lambda x: x.strip().capitalize(), book))


def addition():
    print("Выберите имеющегося автора или добавьте своего", list(authors.keys()))
    author = input()
    if not authors.get(author):
        authors[author] = []
    author_by_books(author)
    print(authors)


while True:
    print("Вы хотите выбрать автора или дополнить список? Выбор/Дополнение")
    choice = input()
    if choice == "Выбор":
        books_by_author()
        break
    if choice == 'Дополнение':
        addition()
        break
    else:
        print("Вы неверно ввели команду!")
        print("Команды: Выбор/Дополнение")
