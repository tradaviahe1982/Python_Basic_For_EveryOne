class Mammal:
    def __init__(self, species):
        self.__species = species
    #
    def show_species(self):
        print("Tôi là: ", self.__species)
    #
    def make_sound(self):
        print('Grrrrrrrrrrrrrrrrrrrrrrrrr')
        