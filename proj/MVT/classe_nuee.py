#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from classe_animal import *
from classe_vecteur import *
from random import random, randint

class Nuee:
    """
    Attributs :
        essaim : liste d'objets de type Animal. Le nombre est donné en paramètre du constructeur
        l_univers, h_univers : entiers, largeur et hauteur
            de l'univers/la grille (en pixels) dans laquelle évolue la nuée
        voisins_proches : tableau de tableaux tel que voisin_proches[i] contient
            la liste de tous les indices des animaux "proches" de l'animal d'indice 'i',
            c'est-à-dire à une distance inférieure à à l'attribut animal.perception[0]
        voisins_moyens : tableau de tableaux tel que voisin_moyens[i] contient
            la liste de tous les indices des animaux "moyennement proches" de l'animal d'indice 'i',
            c'est-à-dire à une distance inférieure à l'attribut animal.perception[1]
        voisins_distants : tableau de tableaux tel que voisin_distants[i] contient
            la liste de tous les indices des animaux "distants" de l'animal d'indice 'i',
            c'est-à-dire à une distance inférieure à l'attribut animal.perception[2]

    Méthodes :
        mouvement :
            Met à jour la position de tous les animaux de la nuée
        voisins_update :
            Met à jour les attributs self.voisins_proches, self.voisins_moyens, et self.voisins_distants
            de sorte que les animaux voisins de l'animal d'indice 'i' aient leurs indices stockés dans voisins[i]
        separation :
            renvoie un vecteur représentant une force permettant aux animaux trop proches d'éviter une collision
        alignement :
            renvoie un vecteur permettant aux animaux moyennement proches de synchroniser leurs vitesses
        cohesion :
            renvoie un vecteur permettant aux animaux distants de se rapprocher
        regles :
            Applique à chaque animal des règles de séparation et/ou d'alignement et/ou de cohésion
            il est conseillé de tester séparément l'application de chaque règle,
            avant de les combiner
    """

    def __init__(self,nombre, l_univers, h_univers):
        self.essaim = []
        # Finir la construction de l'essaim
        for i in range(nombre):
            self.essaim.append(Animal(l_univers, h_univers))
        # trois tableaux contiendront les indices des voisins de chaque animal
        
        # le constructeur initialise ces tableaux, 
        # qui seront mis à jour avec la méthode voisins_update
            
        self.voisins_proches = [[] for i in range(nombre)]
        self.voisins_moyens = [[] for i in range(nombre)]
        self.voisins_distants   = [[] for i in range(nombre)]


    def mouvement(self):
        """Met à jour la position de tous les animaux de la nuée"""
        for animal in self.essaim:
            animal.maj_position()
        retrn self.essaim



    def voisins_update(self) :
        """ met à jour les tableaux
        * self.voisins_proches
        * self.voisins_moyens
        * self.voisins_distants
        de sorte que les animaux voisins de l'animal d'indice 'i'
        aient leurs indices stockés dans voisins[i]
        """
        # A compléter


    def separation(self, indice_animal):
        """ renvoie un vecteur représentant une force permettant aux animaux trop proches
        d'éviter une collision
        """
        liste_voisins = self.voisins_proches[indice_animal]
        animal  = self.essaim[indice_animal]
        force_separation = Vecteur(0, 0)

        return force_separation


    def alignement(self, indice_animal) :
        """ renvoie un vecteur permettant aux animaux moyennement proches de synchroniser leurs vitesses
        * la force renvoyée est la moyenne des vitesses des animaux moyennement proches 
        * si cette force est trop grande, sa norme est ramenée à Animal.force_max
        """
        liste_voisins = self.voisins_moyens[indice_animal]
        animal = self.essaim[indice_animal]
        force_alignement = Vecteur(0, 0)

        return force_alignement


    def cohesion(self, indice_animal):
        """ renvoie un vecteur permettant aux animaux distants de se rapprocher """
        liste_voisins = self.voisins_distants[indice_animal]
        animal = self.essaim[indice_animal]
        force_cohesion = Vecteur(0, 0)

        return force_cohesion

    def regles(self, indice_animal, sep=5, align=0.5, coh=0.01):
        animal = self.essaim[indice_animal]
        if self.voisins_proches[indice_animal] !=[] :
            animal.force.somme(self.separation(indice_animal).prodk(sep))
        elif self.voisins_moyens[indice_animal] !=[]:
            animal.force.somme(self.alignement(indice_animal).prodk(align))
        elif self.voisins_distants[indice_animal] !=[]:
            animal.force.somme(self.cohesion(indice_animal).prodk(coh))
