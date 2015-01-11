#!/usr/bin/python2
#coding: utf-8
from Tkinter import *
from os import getpid,kill
from random import randint

def gaucheH(key):
    global gh,dh
    gh=gh-10
    dh=dh-10
    can.coords(paveJoueurA,gh,00,dh,10)

def droiteH(key):
    global dh,gh
    gh=gh+10
    dh=dh+10
    can.coords(paveJoueurA,gh,00,dh,10)

def gaucheB(key):
    global gb,db
    gb=gb-10
    db=db-10
    can.coords(paveJoueurB,gb,190,db,200)

def droiteB(key):
    global db,gb
    gb=gb+10
    db=db+10
    can.coords(paveJoueurB,gb,190,db,200)

def commencer(key):
    animation()
    lancement.config(text="")

def relancer(key):
    global balleSortie,balle
    balleSortie = False
    can.delete(balle)
    remiseEnJeu.config(text="")
    creation()

def creation():
    global VX,VY,balleX,balleY,balle,hardcore
    direction = randint(0,3)
    if modeHardcore == False:
        if direction == 0:
            VX,VY = 2,2
        if direction == 1:
            VX,VY = -2,2
        if direction == 2:
            VX,VY = 2,-2
        if direction == 3:
            VX,VY = -2,-2
    else:
        VX = randint(-3,3)
        VY = randint(-3,3)
        while VX == 0 or VY == 0:
            VX = randint(-3,3)
            VY = randint(-3,3)
    balleX, balleY = 150,100
    balle = can.create_oval(140,90,160,110,fill="red")

def hardcore(key):
    global modeHardcore
    if modeHardcore == False:
        modeHardcore = True
        hardcoreStatut.config(text = "Mode Hardcore activé")
    else:
        modeHardcore = False
        hardcoreStatut.config(text = "Mode Hardcore désactivé")

def quitter():
    global pid
    kill(pid,9)# Tuer le processus est une façon efficace de fermer le programme

def animation():
    global VX,VY,balleX,balleY,gb,gh,dh,db,scoreHaut,scoreBas,balleSortie,quitter
    futurX,futurY = balleX+VX, balleY+VY
    if (futurX > db+10 or futurX < gb-10) and futurY > 180:
        #Sortie de balle
        scoreHaut += 1
        scoreAfficheHaut.config(text = "Score joueur Haut:" + str(scoreHaut))
        remiseEnJeu.config(text="Appuyer sur Return pour remettre en jeu")
        balleSortie = True
        VX,VY = 0,0
        if scoreHaut == 10:
            # Victoire du haut
            can.delete(ALL)
            can.create_text(150,30,text='Victoire du joueur en haut',fill='green',font=('Comic Sans',16))
            remiseEnJeu.config(text="")
            quitter = Button(fen,text = "Quitter",command=quitter)
            quitter.grid()
        else:
            fen.wait_variable(name='balleSortie')
    if (futurX > dh+10 or futurX < gh-10) and futurY < 20:
        #Sortie de balle
        scoreBas += 1
        scoreAfficheBas.config(text = "Score joueur Bas:" + str(scoreBas))
        remiseEnJeu.config(text="Appuyer sur Return pour remettre en jeu")
        balleSortie = True
        VX,VY = 0,0
        if scoreBas == 10:
            # Victoire du bas
            can.delete(ALL)
            can.create_text(150,30,text='Victoire du joueur en bas',fill='blue',font=('Comic Sans',16))
            remiseEnJeu.config(text="")
            quitter = Button(fen,text = "Quitter",command=quitter)
            quitter.grid()
        else:
          fen.wait_variable(name='balleSortie')
    if futurX > 290 or futurX < 10:
        # S'applique aux murs gauche/droite
        VX = -VX
        futurX = balleX + VX
    elif futurX < dh+10 and futurX > gh-10 and futurY < 20:
        VY = -VY
        futurY = balleY + VY
    elif futurX < db+10 and futurX > gb-10 and futurY > 180:
        VY = -VY
        futurY = balleY + VY
    balleX, balleY = futurX, futurY
    can.coords(balle,balleX - 10,balleY - 10, balleX + 10,balleY + 10)
    if scoreHaut != 10 and scoreBas != 10: # Permet de stopper la fonction à la fin du jeu
        fen.after(20,animation)
scoreHaut = 0
scoreBas = 0
gh = 125
gb = 125
dh = 185
db = 185
modeHardcore = False
fen = Tk()
fen.geometry("300x320")
can = Canvas(fen, width = 300,height = 200,bg="white")
can.grid()
scoreAfficheHaut = Label(fen,text = "")
scoreAfficheBas = Label(fen,text = "")
lancement = Label(fen,text = "Appuyez sur c pour lancer le jeu")
remiseEnJeu = Label(fen,text ="")
hardcoreStatut = Label(fen, text = "Appuyez sur H pour activer le mode hardcore")
scoreAfficheHaut.grid()
scoreAfficheBas.grid()
remiseEnJeu.grid()
lancement.grid()
hardcoreStatut.grid()
creation()
paveJoueurA = can.create_rectangle(gb,00,db,10,fill="green")
paveJoueurB = can.create_rectangle(gh,190,dh,200,fill="blue")
ligneJoueurA = can.create_line(00,10,300,10,fill='#c8c8c8')
ligneJoueurB = can.create_line(00,190,300,190,fill='#c8c8c8')
balleSortie = False
can.focus_set()
can.bind("<Return>",relancer)
can.bind("<c>",commencer)
can.bind("<Left>",gaucheB)
can.bind("<Right>",droiteB)
can.bind("<q>",gaucheH)
can.bind("<d>",droiteH)
can.bind("<h>",hardcore)
pid = getpid()
fen.mainloop()
