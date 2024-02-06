def parcours(depart):
    '''parcours depuis un taquin de depart
    la fonction renvoie un dictionnaire avec
    - comme clés : les configurations accessibles depuis le taquin depart
    - comme valeurs : la configuration immédiatement précédente'''
    dist = {depart:None}
    # à compléter
    
    return dist

def construire_solution(depart):
    """la fonction renvoie la liste des configurations depuis depart jusqu'au taquin final"""
    sol = []
    t = taquin_final
    # a compléter
    return sol

def afficher_solution(depart):
    for s in construire_solution(depart):
        for ligne in s : 
            print(ligne)