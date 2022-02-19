from tkinter import*

def deplace(hauteur=100,longueur=0):
    can.create_oval(hauteur,longueur,10)

fen1=Tk(screenName="Test")
bou1=Button(fen1,text="Quitter",width=5,command=fen1.destroy)
bou1.pack(side=BOTTOM,padx=10,pady=5)
fen1.mainloop()