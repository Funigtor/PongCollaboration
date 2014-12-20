from Tkinter import *
def animation():
    global VX,VY,balleX,balleY
    futurX,futurY = balleX+VX, balleY+VY
    if futurX > 290 or futurX < 10:
        VX = -VX
        futurX = balleX + VX
    if futurY > 190 or futurY < 10:
        VY = -VY
        futurY = balleY + VY
    balleX, balleY = futurX, futurY
    can.coords(balle,balleX - 10,balleY - 10, balleX + 10,balleY + 10)
    fen.after(5,animation)
fen = Tk()
fen.geometry("300x300")
can = Canvas(fen, width = 300,height = 200,bg="white")
can.grid()
VX,VY = 2,2
balleX, balleY = 50,100
balle = can.create_oval(40,90,60,110,fill="red")
pave = can.create_rectangle(gh,gb,dh,db,fill="blue")
animation()
fen.mainloop()

