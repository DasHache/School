from tkinter import  *
from tkinter.messagebox import *

#fenetre
fenetre = Tk()
fenetre.geometry("250x150")
fenetre.title("Banque")

#label
label = Label(fenetre, text="Entre votre numéro de carte (avec espaces) :")
label.pack()

#entree
entree = Entry(fenetre, width = 30)
entree.pack()



def validation():
    chiffres = entree.get()[14 : 19]
    fenetre.withdraw()
    showinfo("Merci!", f"Votre numero de carte: \n **** **** **** {chiffres}")
    fenetre.quit()
    fenetre.destroy()
    
    
    
#bouttons
quitter = Button(fenetre, text="Quitter", command = fenetre.destroy)
quitter.pack(side = RIGHT)
valider = Button(fenetre, text="Valider", command = validation)
valider.pack(side = LEFT)



fenetre.mainloop()

