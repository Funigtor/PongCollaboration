#coding: utf-8
from Tkinter import *
from os import getpid,kill

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
    global VX,VY,balleX,balleY,balle
    VX,VY = 2,2
    balleX, balleY = 50,100
    balle = can.create_oval(40,90,60,110,fill="red")

def quitter():
    global pid
    kill(pid,9)# Tuer le processus est une façon efficace de fermer le programme

def animation():
    global VX,VY,balleX,balleY,gb,gh,dh,db,scoreHaut,scoreBas,balleSortie,quitter
    futurX,futurY = balleX+VX, balleY+VY
    if (futurX > db or futurX < gb) and futurY > 180:
        scoreHaut += 1
        scoreAfficheHaut.config(text = "Score joueur A:" + str(scoreHaut))
        remiseEnJeu.config(text="Appuyer sur Return pour remettre en jeu")
        balleSortie = True
        VX,VY = 0,0
        if scoreHaut == 10:
            # Victoire du haut
            can.delete(ALL)
            can.create_text(150,30,text='Victoire du joueur en haut',fill='green',font=('Comic Sans',18))
            remiseEnJeu.config(text="")
            quitter = Button(fen,text = "Quitter",command=quitter)
            quitter.grid()
        else:
            fen.wait_variable(name='balleSortie')
    if (futurX > dh or futurX < gh) and futurY < 20:
        scoreBas += 1
        scoreAfficheBas.config(text = "Score joueur B:" + str(scoreBas))
        remiseEnJeu.config(text="Appuyer sur Return pour remettre en jeu")
        balleSortie = True
        VX,VY = 0,0
        if scoreBas == 10:
            # Victoire du bas
            can.delete(ALL)
            can.create_text(150,30,text='Victoire du joueur en bas',fill='blue',font=('Comic Sans',18))
            remiseEnJeu.config(text="")
            quitter = Button(fen,text = "Quitter",command=quitter)
            quitter.grid()
        else:
          fen.wait_variable(name='balleSortie')
    if futurX > 290 or futurX < 10:
        # S'applique aux murs gauche/droite
        VX = -VX
        futurX = balleX + VX
    elif futurX < dh and futurX > gh and futurY < 20:
        VY = -VY
        futurY = balleY + VY
    elif futurX < db and futurX > gb and futurY > 180:
        VY = -VY
        futurY = balleY + VY
    balleX, balleY = futurX, futurY
    can.coords(balle,balleX - 10,balleY - 10, balleX + 10,balleY + 10)
    if scoreHaut != 10 and scoreBas != 10: # Permet de stopper la fonction à la fin du jeu
        fen.after(20,animation)
scoreHaut = 0
scoreBas = 0
gh = 130
gb = 130
dh = 180
db = 180
fen = Tk()
fen.geometry("300x340")
can = Canvas(fen, width = 300,height = 200,bg="white")
can.grid()
scoreAfficheHaut = Label(fen,text = "Score joueur A:" + str(scoreHaut))
scoreAfficheBas = Label(fen,text = "Score joueur B:" + str(scoreBas))
lancement = Label(fen,text = "Appuyez sur c pour lancer le jeu")
remiseEnJeu = Label(fen,text ="")
scoreAfficheBas.grid()
scoreAfficheHaut.grid()
remiseEnJeu.grid()
lancement.grid()
creation()
paveJoueurA = can.create_rectangle(gb,00,db,10,fill="green")
paveJoueurB = can.create_rectangle(gh,190,dh,200,fill="blue")
balleSortie = False
can.focus_set()
can.bind("<Return>",relancer)
can.bind("<c>",commencer)
can.bind("<Left>",gaucheB)
can.bind("<Right>",droiteB)
can.bind("<q>",gaucheH)
can.bind("<d>",droiteH)
pid = getpid()
fen.mainloop()
