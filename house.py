class House:
    
    builder = 'eiffage'

    def __init__(self, area = 100): #paramètres à fournir lors de l'utilisation du constructeur
        self.area = area #création d'un attribut area

    def display_area(self):
        print(self.area)

maison1 = House(120) # instanciation, utilise le constructeur
print(f'maison1.area: {maison1.area}')
maison2 = House(70)
print(f'maison2.area: {maison2.area}')
maison1.area = 150
print(f'maison1.area: {maison1.area}')
maison1.display_area()

maison1.price = 10

print(f'prix maison1: {maison1.price}')
print(f'prix maison2: {maison2.price}')