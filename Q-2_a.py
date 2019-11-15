class person():
    def get_gender(self):
        pass
class male(person):
    def get_gender(self):
        print("Male")

class female(person):
    def get_gender(self):
        print("Female")

obj=male()
obj.get_gender()
