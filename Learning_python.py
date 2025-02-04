'''
class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'Hi, I am {self.name}')


person = Person('nandan')
person.talk()

bob = Person("Bob Smith")
bob.talk()
'''
'''
class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    def be_annoying(self):
        print("annoying")


cat1 = Cat()
cat1.be_annoying()
'''

from person_module import walk

