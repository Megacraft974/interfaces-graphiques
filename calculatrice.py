# -*- coding: utf-8 -*-
from tkinter import *

def pointeur(event):
    chaine.configure(text = "Clic détecté en X =" + str(event.x) +", Y =" + str(event.y))

Fen=Tk()
cadre = Frame(Fen, width =200, height =150)
