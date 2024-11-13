# exemple de contenu de filename_input
# 12
# 40
# 4112

# exemple invalide de contenu de filename_input
# a12
# 40
# 4112


def copy_file(filename_input, filename_output):
    pass
    # Cette fonction doit ouvrir le fichier filename_output en mode ajout et écrire le contenu du fichier filename_input dans le fichier
    # A la lecture du fichier filename_input, convertir chaque ligne en entier pour obtenir la somme totale à reporter à la fin du fichier filename_output.

    # Exception 1 :  fichier input introuvable, afficher un message sur la console indiquant que le fichier demandé est introuvable sans provoquer l'arrêt brutal de l'application.

    # Exception 2 : Si le contenu à écrire est invalide (essayer de mettre une valeur numérique), indiquer que le type fourni n'est pas valide sans provoquer l'arrêt brutal de l'application. 

    # Si l'ouverture s'est bien passée, afficher un message indiquant le nombre de caractères qui a été rajouté au fichier.