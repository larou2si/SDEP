import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('employee.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


## use builtin to set attributes into a class
class Person():
    # class variables
    num_of_persones = 0
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@email.com'
        Person.num_of_persones += 1
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
    @classmethod
    def from_string(cls, pers_str):
        first, last, pay = pers_str.split('-')
        return cls(first, last, pay)
    @staticmethod
    def is_workday(day): # !the staticmethod don't take self or cls argument!
        if day.weekday()==5 or day.weekday()==6: # 5 is saturday, 5 sunday
            return False
        return True

    ## decorator, give access to modify a method
    #START Getter, Setter
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split(' ')
    @fullname.deleter
    def fullname(self):
        print('Deleting the name!')
        self.first = None
        self.last = None

    #END Getter, Setter
    ### Special magic Dunder Methods
    def __str__(self) -> str:
        pass
    def __repr__(self) -> str:
        pass


class Developer(Person):
    def __init__(self, first, last, pay):
        super().__init__(first, last, pay)


class Manager(Person):
    def __init__(self, first, last, pay, devs=None):
        super().__init__(first, last, pay)
        if devs is None:
            self.devs = []
        else:
            self.devs = devs


person = Person()
setattr(person, 'key', 'val')
name = getattr(person, 'keyName')
print(name)

emp = Person.from_string('med-ham-1800')

import datetime
print(Person.is_workday(datetime.date(2016, 7, 11)))

print(isinstance(emp, Person))
print(issubclass(Developer, Person))

del emp.fullname ## delete the name, set them to zero!