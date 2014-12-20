from Tkinter import *
def gaucheH(key):
    global gh,dh
    gh=gh-5
    dh=dh-5
    can.coords(paveJoueurB,gh,190,dh,200)
def droiteH(key):
    global dh,gh
    gh=gh+5
    dh=dh+5
    can.coords(paveJoueurB,gh,190,dh,200)
def gaucheB(key):
    global gb,db
    gb=gb-5
    db=db-5
    can.coords(paveJoueurA,gb,10,db,20)

def droiteB(key):
    global db,gb
    gb=gb+5
    db=db+5
    can.coords(paveJoueurA,gb,10,db,20)

def animation():
    global VX,VY,balleX,balleY,gb,gh,dh,db,scoreHaut,scoreBas
    futurX,futurY = balleX+VX, balleY+VY
    if (futurX > db or futurX < gb) and futurY > 190:
        scoreHaut += 1
    if (futurX > dh or futurX < gh) and futurY < 10:
        scoreBas += 1
    if futurX > 290 or futurX < 10:
        # S'applique aux murs gauche/droite
        VX = -VX
        futurX = balleX + VX
    elif futurX < dh and futurX > gh and futurY < 10:
        VY = -VY
        futurY = balleY + VY
    elif futurX < db and futurX > gb and futurY > 190:
        VY = -VY
        futurY = balleY + VY
    balleX, balleY = futurX, futurY
    can.coords(balle,balleX - 10,balleY - 10, balleX + 10,balleY + 10)
    fen.after(15,animation)
scoreHaut = 0
scoreBas = 0
gh = 130
gb = 130
dh = 180
db = 180
fen = Tk()
fen.geometry("300x300")
can = Canvas(fen, width = 300,height = 200,bg="white")
can.grid()
scoreAfficheHaut = Label(fen,text = "Score joueur A:" + str(scoreHaut))
scoreAfficheBas = Label(fen,text = "Score joueur B:" + str(scoreBas))
VX,VY = 2,2
balleX, balleY = 50,100
balle = can.create_oval(40,90,60,110,fill="red")
paveJoueurA = can.create_rectangle(gb,10,db,20,fill="blue")
paveJoueurB = can.create_rectangle(gh,190,dh,200,fill="blue")
animation()
can.focus_set()
can.bind("<Left>",gaucheB)
can.bind("<Right>",droiteB)
can.bind("<q>",gaucheH)
can.bind("<d>",droiteH)
fen.mainloop()
