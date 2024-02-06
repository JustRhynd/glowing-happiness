TAILLE = 3

taquin_final = ((1,2,3),(4,5,6),(7,8,0))

taquin_initial = ((2,6,3),(7,0,5),(4,1,8))


def format_list(taquin_tuple):
    return [[ taquin_tuple[i][j] for j in range(TAILLE)] for i in range(TAILLE)]

def format_tuple(taquin_list): 
    return tuple( tuple( taquin_list[i][j] for j in range(TAILLE)) for i in range(TAILLE))


def haut(taquin,i0,j0):
    """ i0, j0 sont les coordonnées du 0 dans taquin (qui est un tuple)
    la fonction renvoie un nouveau taquin au format tuple dans lequel le 0 a bougé vers le haut """
    taq_list = format_list(taquin)

    if i0 > 0:
        taq_list[i0][j0]   =  taq_list[i0-1][j0]
        taq_list[i0-1][j0] = 0

    return format_tuple(taq_list)


def bas(taquin,i0,j0):
    """  i0, j0 sont les coordonnées du 0 dans taquin (qui est un tuple)
    renvoie un nouveau taquin au format tuple dans lequel le 0 a bougé vers le bas"""
    taq_list = format_list(taquin)

    if i0 < TAILLE-1:
        taq_list[i0][j0]   =  taq_list[i0+1][j0]
        taq_list[i0+1][j0] = 0

    return format_tuple(taq_list)
    

def gauche(taquin,i0,j0):
    """  i0, j0 sont les coordonnées du 0 dans taquin (qui est un tuple)
    renvoie un nouveau taquin au format tuple dans lequel le 0 a bougé vers la gauche"""
    taq_list = format_list(taquin)

    if j0 > 0:
        taq_list[i0][j0]   =  taq_list[i0][j0-1]
        taq_list[i0][j0-1] = 0

    return format_tuple(taq_list)
    

def droite(taquin,i0,j0):
    """  i0, j0 sont les coordonnées du 0 dans taquin (qui est un tuple)
    renvoie un nouveau taquin au format tuple dans lequel le 0 a bougé vers la droite"""
    taq_list = format_list(taquin)

    if j0 < TAILLE-1:
        taq_list[i0][j0]   =  taq_list[i0][j0+1]
        taq_list[i0][j0+1] = 0

    return format_tuple(taq_list)
    
    
def voisins(taquin) : 
    """cherche la position du 0 dans taquin (qui est un tuple)
    et renvoie la liste des configurations voisines"""
    taq_tuple = format_tuple(taquin)
    for i in range(TAILLE):
        for j in range(TAILLE):
            if taq_tuple[i][j] == 0:
                ki, kj = i, j

    resu = []
    if ki > 0:
        resu.append(haut(taq_tuple, ki,kj))
    if ki < TAILLE-1:
        resu.append(bas(taq_tuple, ki,kj))
    if kj > 0:
        resu.append(gauche(taq_tuple, ki,kj))
    if kj < TAILLE-1:
        resu.append(droite(taq_tuple, ki,kj))

    return resu





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