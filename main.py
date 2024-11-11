books = {
    1: {"title": "Звук и ярость", "author": "Уильям Фолкнер", "year": 1929},
    2: {"title": "Человек-невидимка", "author": "Ральф Эллисон", "year": 1952},
    3: {"title": "Война и мир", "author": "Лев Толстой", "year": 1869},
    4: {"title": "Мастер и Маргарита", "author": "Михаил Булгаков", "year": 1967},
    5: {"title": "Уловка-22", "author": " Джозеф Хеллер", "year": 1961}
}
count = 1

for key,book in books.items():
    print("-"*20,"Книга",count,"-"*20)
    print("Название:",book['title'],end=", ")
    print("Автор:",book['author'])
    print("-"*20,book['year'],"-"*20)
    count+=1