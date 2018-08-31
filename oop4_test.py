from oop4_polymorphism import Mammal
from oop4_polymorphism_Cat import Cat
from oop4_polymorphism_Dog import Dog
def main():
    mammal = Mammal("Động vật")
    dog = Dog()
    cat = Cat()
    dog.show_species()
    dog.make_sound()
    #
    cat.show_species()
    cat.make_sound()
#
main()
