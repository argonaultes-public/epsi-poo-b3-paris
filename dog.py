class Dog:

    kind = 'canine'

    def __init__(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name

class CircusDog(Dog):

    def __init__(self, name):
        super().__init__(name)
        self.__tricks = []

    def add_trick(self, trick):
        self.__tricks.append(trick)