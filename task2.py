class CountError(Exception):
    def __init__(self, mes):
        self.mes = mes


class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return f'{self.surname} {self.name}, {self.age}'


class Student(Person):
    def __init__(self, name, surname, age, fac):
        super().__init__(name, surname, age)
        self.fac = fac

    def __str__(self):
        return f'{self.surname} {self.name[0]}.: {self.age}, {self.fac}'


class Group:
    def __init__(self, group: list):
        self.group = group
        count = 0
        for item in self.group:
            count += 1
            if count > 10:
                raise CountError('only 10 students can be in one group')

    def add_student(self, value: Student):
        self.group.append(value)

    def remove_student(self, value: Student):
        self.group.remove(value)

    def student_search(self, surname):
        res = []
        for stud in self.group:
            if stud.surname == surname:
                res.append(stud)
        return res or None

    def __str__(self):
        group_tmp = "\n".join(map(str, self.group))
        return f'{group_tmp}\n'


per1 = Person('Ivan', 'Ivanov', 25)
per2 = Student('Petr', 'Petrov', 23, 'math')

st1 = Student('Ivan', 'Ivanov', 25, 'math')
st2 = Student('Ivan', 'Petrov', 25, 'science')
st3 = Student('Ivan', 'Markov', 25, 'history')
st4 = Student('Ivan', 'Sidorov', 25, 'math')
st5 = Student('Ivan', 'Vlasov', 25, 'science')
st6 = Student('Maria', 'Ivanova', 25, 'math')
st7 = Student('Maria', 'Petrova', 25, 'art')
st8 = Student('Maria', 'Markova', 25, 'history')
st9 = Student('Maria', 'Sidorova', 25, 'art')
st10 = Student('Maria', 'Vlasova', 25, 'math')
st11 = Student('Maria', 'Vlasova', 25, 'math')


group1 = Group([st1, st2, st3, st4, st5, st6, st7, st8, st9, st10])

print(group1.student_search('Sidorova'))
print(per1)
print(per2)
print(group1)
