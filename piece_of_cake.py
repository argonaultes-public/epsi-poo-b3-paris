# partir du gateau

cake = 'abcabcabcabc'

def piece_of_cake(cake):

    # prendre pour référence le 1er caractère - 1 m&ms par part
    for size_slice_ref in range(1, len(cake)):
        isvalid = True

        slice_ref = cake[0:size_slice_ref] #part de taille 1

        # comparer avec tous les autres caractères
        
        for slice_idx in range(0, len(cake), size_slice_ref):
        # si j'ai une différence, alors il faut augmenter le nombre de mms - augmenter la taille de la part
            if slice_ref != cake[slice_idx:slice_idx + size_slice_ref]:
                isvalid = False
        if isvalid:
            return int(len(cake) / size_slice_ref)
    # si j'ai pas de différence, que j'arrive au bout de la chaine de caractère, le nombre de mms, la taille de la part est valide
    return 1
    #size_slice_ref = len(slice_ref)

    # pour trouver le nombre de parts, en connaissant la taille d'une part et le taille du gateau : taille du gateau / taille d'une part => nb de parts

if __name__ == '__main__':
    print(piece_of_cake('abcabcabcabc'))