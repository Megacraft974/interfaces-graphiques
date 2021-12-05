from tkinter import *
import os

def getCredentials(infos):
	fen = Tk()

	Label(fen, text="NNI:").grid(row=0,column=0,sticky="nsw",padx=(10,0),pady=(10,0))
	login = StringVar(fen)
	login.set(os.getlogin())
	Entry(fen, textvariable=login).grid(row=0,column=1,sticky="nsew",padx=(0,10),pady=(10,0))

	Label(fen, text="Mot de passe:").grid(row=1,column=0,sticky="nsw",padx=(10,0))
	password = StringVar(fen)
	Entry(fen, textvariable=password, show="*").grid(row=1,column=1,sticky="nsew",padx=(0,10))

	option = IntVar()
	option.set(2)
	Radiobutton(fen, text="Superutilisateur", variable=option, value="1").grid(row=2,column=0,pady=(10,0),padx=(10,0))
	Radiobutton(fen, text="Standard", variable=option, value="2").grid(row=2,column=1,pady=(10,0))

	Label(fen, text=infos).grid(row=3,column=0,columnspan=2,sticky="nsew",pady=10)

	Button(fen, text="Valider", bg="orange", command=fen.quit).grid(row=4,column=0,columnspan=2,pady=10)


	[fen.grid_columnconfigure(i,weight=1) for i in range(2)]
	fen.mainloop()

	return login.get(), password.get(), "Superutilisateur" if option.get() == 1 else "Standard"

if __name__ == "__main__":
	login, password, option = getCredentials("dmaijfemqsejgf^mq")

	print("Login:",login)
	print("Password:",password)
	print("Option:",option)