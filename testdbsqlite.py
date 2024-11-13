import sqlite3

# création du fichier de bdd s'il nexiste pas
connection = sqlite3.connect('movies.db')

# obtention d'un cursor nécessaire pour l'exécution de requêtes
cursor = connection.cursor()

# créer une nouvelle table
try:
    result = cursor.execute('CREATE TABLE movies(title)')
except:
    pass

# prépare une liste de films à insérer
best_movies = [
    ('tenet',),
    ('interstellar',),
    ('inception',)
]
print(best_movies)
# insertion des données avec executemany
cursor.executemany('INSERT INTO movies VALUES (?)', best_movies)
connection.commit()

# vérifier le résultat avec un select
result_movies = cursor.execute('SELECT title FROM movies')

# utilisation du fetchall pour récupérer dans une liste les résultats
all_movies = result_movies.fetchall()
print(type(all_movies[0]))
print(all_movies)

