#!usr/bin/env python3
import datetime
class Employee:
    num_of_emp = 0
    raise_amount = 1.04 # raise_amout is called a class variable

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay
        Employee.num_of_emp += 1

    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay *= self.raise_amount
 
    @classmethod # using a class method will take the class as the first argument instead of an instance
    def set_raise_amount(cls, amount): #classmethod is often defined when need to change class variable
        cls.raise_amount = amount # for eg: we'd like to change raise_amount

    @classmethod
    def from_string(cls, emp_string):
        # this is another way to initialize a new class (an alternative constructure)
        # think how can I apply this to my own project Door-to-door
        first, name, pay = emp_string.split('-')
        return cls(first, name, pay)
    
    @staticmethod
    def is_workday(day):
        # static methods dont operate on instance or class
        # it does not take any instance virable of class variable, but still
        # have logical connection with this Employee class        
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True 
    
    def __repr__(self):
        return "Employee('{}','{}',{})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} {}'.format(self.full_name(), self.email)
    
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.full_name())

# e1, e2 is called instance
emp_1 = Employee('Trung', 'Nguyen', 75000)
emp_2 = Employee('Nathan', 'Trump', 90000) 
# =====================
# these lines below is for examples of using class method to initialize
# def from_string() above
""" emp_1 = 'Joe-Doe-70000'
emp_2 = 'Steve-Smith-30000'
emp_3 = 'Jane-Doe-90000' """

""" new_emp_1 = Employee.from_string(emp_1)
print(new_emp_1.__dict__) """
# =====================
# static method
'''my_date = datetime.date(2020, 2, 29)
print(Employee.is_workday(my_date))'''
# =====================
# VIDEO 4 INHERITANCE
# =====================
'''
Inheritance allows us to use attributes and method from parents class
'''
class Developer(Employee):
    # class Developer will look for raise_amount first in its own class
    # if it's not there it will look in its parent class Employee
    raise_amount = 1.1
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) #we dont want to repeat the code so let's inherit it from parent class
        # Employee.__init__(self, first, last, pay) => some people use this way
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None): # the reason to pass None as default argument is because we 
        super().__init__(first, last, pay) # dont want to pass mutable input like list as arguments
        if employees is None:  
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self, emp): # think how can we apply this to the project
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.full_name())

dev_1 = Developer('Trung', 'Nguyen', 50000, 'Python')
dev_2 = Developer('Nathan', 'Trump', 100000, 'Java')

""" mgr_1 = Manager('Tech', 'Lead', 200000, [dev_1])
mgr_1.add_emp(dev_2)
print(mgr_1.email)
mgr_1.print_emps()

print(dev_1.email)
print(dev_1.prog_lang)repr(emp_1)


print(dev_1.email)
print(dev_2.email)
print(help(Employee))

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)  """
# =======================================
# VIDEO 5: Special (Magic/Dunder) Methods
# =======================================

""" print(repr(emp_1))
print(str(emp_1))
print(emp_1 + emp_2)

print(len(emp_1)) """

# =============================================================
# VIDEO 6: Property Decorators - Getters, Setters, and Deleters
# =============================================================

