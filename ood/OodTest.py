class Interface1:
    def say_hello(self):
        pass

class Parent:
    def sing(self):
        print("Parent sing!")


class Child(Parent, Interface1):
    def __init__(self, name):
        self.name = name

    def sing(self):
        super().sing()
        print(f"{self.name} sings")
        raise CustomException()

class CustomException(Exception):
    pass

if __name__ == '__main__':
    s = Child("linfeng")
    s.sing()
    s.say_hello()
