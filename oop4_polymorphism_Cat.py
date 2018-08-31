from oop4_polymorphism import Mammal
class Cat(Mammal):
    def __init__(self):
        Mammal.__init__(self, "Cat")
    #
    def make_sound(self):
        print("Meowowowowowowowowow!!! Meowowowowoowowowowo !!!")
    #