# -*- coding: utf-8 -*-
import tkinter
import time
from random import randint, random
from math import sqrt, cos, sin, pi, asin, acos
from classe_nuee import *


LARGEUR_FENETRE = 1300
HAUTEUR_FENETRE = 700
RAFRAICHISSEMENT = 0.01
AFFICHE_VOISINS = True 


def animate_ball(nuee):
    global canvas, fenetre

    taille = nuee.essaim[0].taille
    sprites = []
    for i in range(len( nuee.essaim)):
         sprites.append(canvas.create_oval(nuee.essaim[i].position.x - taille,
            nuee.essaim[i].position.y - taille,
            nuee.essaim[i].position.x + taille,
            nuee.essaim[i].position.y + taille,
            fill="Black", outline="Black",
            width=1))


    if AFFICHE_VOISINS :
        canvas.itemconfig(sprites[0], fill='red', outline = "red",
                        width = 2)
        cercle_0 = canvas.create_oval(
                nuee.essaim[0].position.x - nuee.essaim[0].perception[0],
                nuee.essaim[0].position.y - nuee.essaim[0].perception[0],
                nuee.essaim[0].position.x + nuee.essaim[0].perception[0],
                nuee.essaim[0].position.y + nuee.essaim[0].perception[0],
                outline="red", width=1)
        cercle_1 = canvas.create_oval(
                nuee.essaim[0].position.x - nuee.essaim[0].perception[1],
                nuee.essaim[0].position.y - nuee.essaim[0].perception[1],
                nuee.essaim[0].position.x + nuee.essaim[0].perception[1],
                nuee.essaim[0].position.y + nuee.essaim[0].perception[1],
                outline="blue", width=1)
        cercle_2 = canvas.create_oval(
                nuee.essaim[0].position.x - nuee.essaim[0].perception[2],
                nuee.essaim[0].position.y - nuee.essaim[0].perception[2],
                nuee.essaim[0].position.x + nuee.essaim[0].perception[2],
                nuee.essaim[0].position.y + nuee.essaim[0].perception[2],
                outline="magenta", width=1)


    while True :

        mvts = nuee.mouvement()
        if len(mvts) != len(sprites):

            raise IndexError("pas le même nombre de sprites et d'animaux")

        # Test des voisins : enlever les triples guillemets pour le bloc ci-dessous
        if AFFICHE_VOISINS :
            for i in range(1, len(nuee.essaim)):
                if i in nuee.voisins_proches[0] :
                    canvas.itemconfig(sprites[i], fill='red', outline = 'red', width = 1)
                elif i in nuee.voisins_moyens[0]:
                    canvas.itemconfig(sprites[i], fill='blue', outline = 'blue', width = 1) # color
                elif i in nuee.voisins_distants[0] :
                    canvas.itemconfig(sprites[i], fill='magenta', outline = 'magenta', width = 1)
                else :
                    canvas.itemconfig(sprites[i], fill='black', outline="Black", width=1)

        for i in range(len(mvts)) :
            canvas.coords(sprites[i],
                          nuee.essaim[i].position.x - taille,
                          nuee.essaim[i].position.y - taille,
                          nuee.essaim[i].position.x + taille,
                          nuee.essaim[i].position.y + taille)

        if AFFICHE_VOISINS:
            canvas.coords(cercle_0,
                        nuee.essaim[0].position.x - nuee.essaim[0].perception[0],
                        nuee.essaim[0].position.y - nuee.essaim[0].perception[0],
                        nuee.essaim[0].position.x + nuee.essaim[0].perception[0],
                        nuee.essaim[0].position.y + nuee.essaim[0].perception[0])
            canvas.coords(cercle_1,
                        nuee.essaim[0].position.x - nuee.essaim[0].perception[1],
                        nuee.essaim[0].position.y - nuee.essaim[0].perception[1],
                        nuee.essaim[0].position.x + nuee.essaim[0].perception[1],
                        nuee.essaim[0].position.y + nuee.essaim[0].perception[1])
            canvas.coords(cercle_2,
                        nuee.essaim[0].position.x - nuee.essaim[0].perception[2],
                        nuee.essaim[0].position.y - nuee.essaim[0].perception[2],
                        nuee.essaim[0].position.x + nuee.essaim[0].perception[2],
                        nuee.essaim[0].position.y + nuee.essaim[0].perception[2])

        fenetre.update()
        time.sleep(RAFRAICHISSEMENT)

l_univers = LARGEUR_FENETRE - 100
h_univers = HAUTEUR_FENETRE - 100
nuee = Nuee(20, l_univers, h_univers)       # nombre d'animaux à modifier suivant puissance de l'ordi


fenetre = tkinter.Tk()
fenetre.title("Nuée d'oiseaux / banc de poisson / essaim d'insectes")
fenetre.geometry(f'{LARGEUR_FENETRE}x{HAUTEUR_FENETRE}')

canvas = tkinter.Canvas(fenetre, width = l_univers, height = h_univers, bg = "cyan")
canvas.pack(anchor = tkinter.CENTER, expand=True)

animate_ball(nuee)