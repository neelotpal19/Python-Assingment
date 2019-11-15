from abc import ABC, abstractmethod
class person(ABC):
    @abstractmethod
    def get_gender(self):
        pass
class male(person):
    def get_gender(self):
        print("Male")

class female(person):
    def get_gender(self):
        print("Female")
try:
    obj=person()
    obj.get_gender()
except TypeError as e:
    print("Error: ",e)
