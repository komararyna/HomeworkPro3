class Book:
    def __init__(self, name, autor, year, izd, quan):
        self.name = name
        self.autor = autor
        self.izd = izd
        self.year = year
        self.quan = quan

    def __str__(self):
        return f'{self.name}, {self.autor}: {self.year}, {self.izd}, {self.quan} страниц'


class Library:
    def __init__(self, group: list):
        self.group = group

    def book_search(self, year):
        res = []
        for book in self.group:
            if book.year == year:
                res.append(book)
        return res or None

    def __str__(self):
        group_tmp = "\n".join(map(str, self.group))
        return f'{group_tmp}\n'


book1 = Book('Дориан Грей', 'О. Уайлд', 2010, 'НФ', 256)
book2 = Book('451 градус по фаренгейту', 'Р. Бредбери', 2008, 'НФ', 212)
book3 = Book('Преступление и наказание', 'Ф. Достоевский', 2012, 'ТК', 657)
book4 = Book('Прислуга', 'К. Стокетт', 2010, 'НФ', 347)
book5 = Book('Твой стиль', 'К. Туск', 2010, 'ТК', 285)

lib = Library([book1, book2, book3, book4, book5])

print(lib)
print(lib.book_search(2010))
