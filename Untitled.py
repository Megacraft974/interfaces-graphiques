from tkinter import *
def pointeur(event):
    chaine.configure(text = "Clic détecté en X =" + str(event.x) + ", Y =" + str(event.y))

fen = Tk()
cadre = Frame(fen, width =500, height =500, bg="light yellow")
cadre.bind("<Button-1>", pointeur)
cadre.pack()
chaine = Label(fen)
chaine.pack()
fen.mainloop()
