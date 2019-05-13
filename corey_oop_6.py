#!usr/bin/env python3

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    
    @property # with property decorator, we can define a method but can access it as an atrribute
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Deleter eheehe!')
        self.first = None
        self.last = None
        self.pay = None  
    

emp_1 = Employee('John', 'Wick', 690000)
emp_1.fullname ='Nathan Trump'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname
print(emp_1.__dict__)
