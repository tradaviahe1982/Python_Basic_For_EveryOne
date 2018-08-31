from oop4_polymorphism import Mammal
class Dog(Mammal):
    def __init__(self):
        Mammal.__init__(self, "Dog")
    #
    def make_sound(self):
        print("Wooooooooooooof!!! Woooooooooooooof !!!")
    #