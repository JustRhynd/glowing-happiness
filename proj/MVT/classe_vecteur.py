from math import sqrt, cos, sin, acos, asin, atan2, pi

class Vecteur:
    """
    Une classe pour gérer plus facilement les opérations sur les vecteurs (en 2 dimensions)
    Attributs :
        x flottant, coordonnée du vecteur suivant (Ox)
        y flottant, coordonnée du vecteur suivant (Oy)
    
    Méthodes :
        est_nul() :     renvoie un booléne Vrai si le vecteur est nul et faux sinon
        vect_nul() :    met les coordonnées du vecteur à 0
        norme() :       renvoie la norme du vecteur (sa longueur)
        somme(v) :      transforme le vecteur courant self en self + v (ajout de vecteurs) 
                        et renvoie le vecteur obtenu
        diff(v) :       transforme le vecteur courant self en self - v (soustraction de vecteurs)
                        et renvoie le vecteur obtenu
        oppose() :      transforme le vecteur courant self en -self
                        et renvoie le vecteur obtenu
        prodk(k):       transforme le vecteur courant self en k*self (produit d'un vecteur par une constante)
                        et renvoie le vecteur obtenu
        affectation(v): Affecte les coordonnées de v à celle du vecteur courant self
                        et renvoie le vecteur obtenu
        est_egal(v) :   Renvoie un booléen Vrai si les deux vecteurs sont égaux
        normalisation(): transforme le vecteur courant self en un vecteur de même sens et direction,
                        mais de norme 1. Le vecteur doit avoir une norme non nulle.
                        Méthode : on divise les coordonnées du vecteur par sa norme
        
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def est_nul(self):
        if self.x == 0 and self.y == 0 :
            return True
        else :
        return False
    
    def vect_nul(self):
        self.x = 0
        self.y = 0
        return self.x, self.y
    
    def norme(self):
        return sqrt(self.x**2 + self.y**2)
        
    def somme(self, v):
        self.x = self.x + v.x
        self.y = self.y + v.y
        return self 
    
    def diff(self, v):
        self.x = self.x - v.x
        self.y = self.y - v.y
        return self 
    
    def oppose(self):
        self.x = -self.x
        self.y = -self.y
        return self.x, self.y
        
    def prodk(self, k):
        self.x = k*self.x
        self.y = k*self.y
        return self.x, self.y

    def affectation(self, v):
        self.x = v.x
        self.y = v.y
        return self.x, self.y
    
    def est_egal(self, v):
        return self.x == v.x and self.y == v.y
    
    def normalisation(self):
        # Transforme le vecteur courant en un vecteur de norme 1. Opération très courante
        # même s'il est probable que c'est la première fois que vous entendez ce terme
        # Si le vecteur est nul, on ne peut pas le normaliser => on affiche un message
        # d'erreur dans ce cas. Si on veut arreter le programme, on peut remplacer le test par : 
        # assert norme != 0 , "ERREUR : erreur de normalisation, vecteur nul" 
        # ou encore
        # if norme == 0 : 
        #   raise ValueError('ERREUR : erreur de normalisation, vecteur nul')
        
        norme = self.norme()
        if norme == 0 :
            print("AVERTISSEMENT : erreur de normalisation, vecteur nul")
        else :
            self.x = self.x/norme
            self.y = self.y/norme
    

    
    def __repr__(self):
        return "(" + str(self.x) + " , " + str(self.y) + ")"

def tests():    
    u = Vecteur(1, 2)
    v = Vecteur(3, 4)
    print("vecteur u : ", u)
    print("vecteur v : ", v)
    u.somme(v)
    print("somme u + v : ", u)
    u.prodk(3)
    print("produit 3u : ", u)
    print("Norme de v : ", v.norme())
    print("u est-il nul : ",u.est_nul())
    u.vect_nul()
    print("Test de la mise au vecteur nul de u : ", u.est_nul())
    u.affectation(v)
    print("Vecteur u après lui avoir affecté v : ", u)
    u.oppose()
    print("Opposé de u :", u)
    u.diff(v)
    print("Calcul u - v : ", u)
    v = Vecteur(2, 2)
    print("Vecteur v", v)
    v.normalisation()
    print("Vecteur v normalisé :", v)
