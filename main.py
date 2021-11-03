class InputError(Exception):
    def __init__(self, exp, mes):
        self.exp = exp
        self.mes = mes


class Price:
    def __init__(self, num):
        for item in str(num):
            if item.isalpha():
                raise InputError(num, 'number should be without letters')
        if int(num) <= 0:
            raise InputError(num, 'number should be bigger than zero')
        self.num = num

    def __str__(self):
        return f'{self.num}'


try:
    num = (input('insert price:'))
except InputError as err:
    print(err)
obj1 = Price(num)