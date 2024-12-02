import sqlite3
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
        self.__connection = sqlite3.connect('race.db')

    @property
    def distance(self):
        return self.__distance

    @distance.setter
    def distance(self, new_distance):
        self.__distance = new_distance

    @property
    def vitesse_max(self):
        return self.__vitesse_max

    @property
    def latence(self):
        return self.__latence


    def save_in_db(self):
        # INSERT INTO distance_historique (nom_vaisseau, couleur_du_vaisseau, vitesse_max, latence, distance, classement)
        cursor = self.__connection.cursor()
        cursor.execute('INSERT INTO distance_historique (nom_vaisseau, couleur, vitesse_max, latence, distance, classement) VALUES (?, ?, ?, ?, ?, ?)', (
            self.__nom,
            self.__couleur,
            self.__vitesse_max,
            self.__latence,
            self.__distance,
            self.__classement
        ))
        self.__connection.commit()

    def __eq__(self, other):
        return self.__nom == other.__nom and self.__couleur == other.__couleur

    def __hash__(self):
        return hash((self.__nom, self.__couleur))


    def __repr__(self) -> str:
        return f'[{self.__nom}, {self.__couleur}, vmax: {self.__vitesse_max}, cl: {self.__classement}, d: {self.__distance}, l: {self.__latence}]'

class Circuit:

    def __init__(self, nb_tours, distance):
        self.__nb_tours = nb_tours
        self.__distance = distance
    
    @property
    def total_distance(self):
        return self.__nb_tours * self.__distance

class Course:

    def __init__(self, circuit):
        self.__circuit = circuit
        self.__vaisseaux = set()
        self.__nb_ticks = 0
        # list() []
        # tuple() : Non
        # set() : chaque élément est unique
        #self.init_db()
    
    def init_db(self):
        
        connection = sqlite3.connect('race.db')
        cursor = connection.cursor()
        try:
            cursor.execute('CREATE TABLE distance_historique (nom_vaisseau, couleur, vitesse_max, latence, distance, classement)')
        except:
            print('Table distance_historique existe déjà')
            cursor.execute('TRUNCATE TABLE distance_historique')

    def inscrire_vaisseau(self, vaisseau : Vaisseau):
        self.__vaisseaux.add(vaisseau)

    # 1 nouvelle second passe
    def tick(self):
        print(f'Tick nb {self.__nb_ticks}')
        for v in self.__vaisseaux:
            # si self.__nb_ticks < v.latence, alors le vaisseau reste immobile
            # si self.__nb_ticks > v.latence, alors le vaisseau peut avancer
            # v.distance + (vitesse * t) = v.distance + v.vitesse_max
            print(v)
            if self.__nb_ticks > v.latence:
                v.distance = v.distance + v.vitesse_max

            # sauvegarder en bdd la position du vaisseau
            #v.save_in_db()

        # le temps avance d'1 seconde
        self.__nb_ticks = self.__nb_ticks + 1

    def run(self):
        winners = set()
        while len(winners) == 0:
            self.tick()
            # solution 0
            # for v in self.__vaisseaux:
            #     if v.distance > self.__circuit.total_distance:
            #         winners.add(v)
            # solution 1: list comprehension
            # a = {x for x in 'abracadabra' if x not in 'abc'}
            # winners = {v for v in self.__vaisseaux if v.distance > self.__circuit.total_distance}
            # solution 2: filter / lambda
            winners = set(filter(lambda v: v.distance > self.__circuit.total_distance, self.__vaisseaux))

        return winners               

    # définir le classement 

    def __repr__(self) -> str:
        return str(self.__vaisseaux)

# class Position:
#     def __init__(self):
#         pass

if __name__ == '__main__':
    circuit = Circuit(2, 2000)
    v1 = Vaisseau('vaisseau', 'red', 100, 20)
    v2 = Vaisseau('vaisseau', 'bleu', 150, 28)
    v3 = Vaisseau('vaisseau', 'noir', 10, 0)

    course = Course(circuit)
    course.inscrire_vaisseau(v1)
    course.inscrire_vaisseau(v2)
    course.inscrire_vaisseau(v3)
    winners = course.run()
    print(winners)
