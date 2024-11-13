# Créer une classe moldu qui a un attribut nom
class Moldu:
    def __init__(self, nom):
        self.__nom = nom
    
    def get_nom(self):
        return self.__nom

    def set_nom(self, value):
        self.__nom = value

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        self.__nom = value

# Créer une classe sorcier qui a un attribut maison
# Faire en sorte que la classe sorcier hérite de la classe moldu
class Sorcier(Moldu):
    def __init__(self, nom, maison):
        super().__init__(nom)
        self.__maison = maison
# Ajouter une méthode lancer_un_sort à la classe Sorcier.

    def lancer_un_sort(self):
# La méthode lancer_un_sort() affiche Lancer un sort par {nom_du_sorcier}
        print(f'Lancer un sort par {self.nom}')


# Créer une instance de sorcier
# Créer une instance de moldu
jean = Moldu('jean')
harry = Sorcier('harry', 'g')


# Tenter de lancer un sort depuis l'instance du sorcier.
harry.lancer_un_sort()
# Tenter de lancer un sort depuis l'instance du moldu.
jean.lancer_un_sort()
