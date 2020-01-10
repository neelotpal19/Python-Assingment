'''Python Assignment Q-2'''
# pylint: disable=too-few-public-methods
# pylint: disable=E0110
from abc import ABC, abstractmethod
class Person(ABC):
    ''' Parent Class'''
    @abstractmethod
    def get_gender(self):
        ''' Abstract Method'''
class Fale(Person):
    ''' Child Class'''
    def get_gender(self):
        ''' Method return male'''
        print("Male")

class Female(Person):
    ''' Child Class'''
    def get_gender(self):
        ''' Method return female'''
        print("Female")
try:
    PERSON_OBJ = Person()
    PERSON_OBJ.get_gender()
except TypeError as error_msg:
    print("Error: ", error_msg)
