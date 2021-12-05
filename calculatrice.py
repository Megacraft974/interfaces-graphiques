# -*- coding: utf-8 -*-
from tkinter import *

def pointeur(event):
    chaine.configure(text = "Clic détecté en X =" + str(event.x) +\", Y =" + str(event.y))

Fen1=Tk()
cadre = Frame(Fen, width =200, heigt =150,
