from classe_vecteur import *
from random import random, randint

class Animal:
    """
    Attribut de classe :
        v_max : norme maximale du vecteur vitesse
        v_init : norme du vecteur vitesse lors de la création de l'objet
        force_max = force maximale s'exerçant sur l'animal. Pour un comportement réaliste,
                    un animal ne peut pas par exemple faire un demi-tour immédiatement
    Attributs :

        position :      vecteur de coordonnées x, y aléatoires, dans les limites de la fenêtre d'affichage
        vitesse :       vecteur  sous la forme d'une liste de flottants
        taille :        rayon en pixels de l'animal. C'est comme en physique, tout est
                         une sphère parfaite (ici un cercle puisqu'en 2D)
        perception :    liste des rayons de perception de l'animal. Noter que l'animal ne
            perçoit pas ce qui se passe derrière lui. On suppose qu'il a une
            vision à 300 degrés, soit +/- 150 degrés par rapport à sa direction.
            La liste comprend 3 éléments qui correspondent aux trois règles de déplacement.

    Méthodes :
        force_alea : crée une force de déplacement aléatoire qui va
                    s'appliquer sur l'animal
        maj_position : déplace l'animal suivant sa vitesse.
        distance : revoie la distance avec un autre Animal

    """
    v_max = 4
    v_init = 2
    force_max = 1

    def __init__(self, l_univers, h_univers):
        self.taille = 2
        self.l_univers = l_univers
        self.h_univers = h_univers
        # Modifier les deux lignes suivantes
        x = randint(0, self.l_univers)
        y = randint(0, self.h_univers)
        self.position = Vecteur(x, y)
        self.vitesse = Vecteur(0, 0)
        # Modifier les deux lignes après le while
        while self.vitesse.est_nul() :          # génération d'une vitesse aléatoire
            self.vitesse.x = random()
            self.vitesse.y = random()
        self.vitesse.prodk(self.v_init/self.vitesse.norme()) # on met la norme de la vitesse à v_init
        self.perception = [30, 100, 200]     # proche, moyen, distant
        self.force = Vecteur(0, 0)

    def force_alea(self):
        self.force.x = random() - 0.5
        self.force.y = random() - 0.5

        if self.force.norme() != 0 :
            self.force.prodk(self.force_max/self.force.norme())

        return self.force

    def maj_position(self):
        #self.force_alea()            # test avec une force aléatoire (question 2b)
        self.position.x += self.vitesse.x
        self.position.y += self.vitesse.y
        if self.position.x < 0 or self.position.x > self.l_univers :
            self.vitesse.x = -self.vitesse.x
        if self.position.y < 0 or self.position.y > self.h_univers :
            self.vitesse.y = -self.vitesse.y
        self.vitesse.x += self.force.x
        self.vitesse.y += self.force.y
        if self.vitesse.norme() > self.v_max :
            self.vitesse.prodk(self.v_max/self.vitesse.norme())

        #self.force_alea()
        return self.position

    def distance(self, autre):
        return sqrt((autre.position.x - self.position.x)**2 + (autre.position.y - self.position.y)**2)

    def __repr__(self):
        chaine = "Position : (" + str(self.position.x) + " , " + str(self.position.y) + ")\n"
        chaine += "Vitesse : (" + str(self.vitesse.x)  + " , " + str(self.vitesse.y) + ")\n"
        chaine += "Acceleration/force : (" + str(self.force.x)  + " , " + str(self.force.y) + ")\n"
        return chaine