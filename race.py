
## Exercice des vaisseaux

# Vous devez modéliser une course de vaisseaux spatiaux.
# Ces vaisseaux ont comme particularité un nom, une couleur, une vitesse plateau (m/s) et une latence (s).
# Les vaisseaux évoluent sur un circuit qui a une distance en mètres et un nombre de tours.
# Pour une course donnée, à chaque tick (s), indiquer la position (classement par rapport aux autres) des vaisseaux.
# Sauvegarder la position des vaisseaux en BDD à chaque tick.

class Vaisseau:

    def __init__(self, nom, couleur, vitesse_max, latence):
        self.__nom = nom
        self.__couleur = couleur
        self.__vitesse_max = vitesse_max
        self.__latence = latence
        self.__distance = 0
        self.__classement = 0

class Circuit:

    def __init__(self, nb_tours, distance):
        self.__nb_tours = nb_tours
        self.__distance = distance

class Course:

    def __init__(self, circuit, vaisseaux):
        self.__circuit = circuit
        self.__vaisseaux = vaisseaux

    def tick(self):
        # incrémenter la distance parcourue d'un vaisseau
        pass

class Position:
    def __init__(self):
        pass