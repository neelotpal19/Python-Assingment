'''Python Assignment Q-1'''
# pylint: disable=too-few-public-methods
class Person():
    ''' Parent Class'''
    def get_gender(self):
        ''' Empty method'''
class Male(Person):
    ''' Child Class'''
    def get_gender(self):
        ''' Method return male'''
        print("Male")
class Female(Person):
    ''' Child Class'''
    def get_gender(self):
        ''' Method return female'''
        print("Female")
OBJ = Male()
OBJ.get_gender()
