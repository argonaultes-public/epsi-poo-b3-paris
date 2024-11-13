# exemple de contenu de filename_input
# 12
# 40
# 4112

# exemple invalide de contenu de filename_input
# a12
# 40
# 4112


def copy_file(filename_input, filename_output):
    result = 0
    # Cette fonction doit ouvrir le fichier filename_output en mode ajout et écrire le contenu du fichier filename_input dans le fichier
    try:
        fileinput = open(filename_input, 'r')
        fileoutput = open(filename_output, 'a')
        # A la lecture du fichier filename_input, convertir chaque ligne en entier pour obtenir la somme totale à reporter à la fin du fichier filename_output.
        for line in fileinput.readlines():
            result = result + int(line.strip())
            fileoutput.write(line)
        fileoutput.write('\n')
        fileoutput.write(str(result))
        fileoutput.write('\n')
    except FileNotFoundError:
        print(f'Impossible de trouver le fichier {filename_input}')
    except ValueError:
        print('Impossible de convertir la ligne en entier.')
    # Exception 1 :  fichier input introuvable, afficher un message sur la console indiquant que le fichier demandé est introuvable sans provoquer l'arrêt brutal de l'application.

    # Exception 2 : Si le contenu à écrire est invalide (essayer de mettre une valeur numérique), indiquer que le type fourni n'est pas valide sans provoquer l'arrêt brutal de l'application. 

    # Si l'ouverture s'est bien passée, afficher un message indiquant le nombre de caractères qui a été rajouté au fichier.

if __name__ == '__main__':
    copy_file('fileinput_valid.txt', 'fileoutput.txt')
    copy_file('doesnotexist.txt', 'fileoutput.txt')
    copy_file('fileinput_invalid.txt', 'fileoutput.txt')
    copy_file('fileinput_valid.txt', 'fileoutput.txt')
