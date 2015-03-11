# widgets Button and Label
from Tkinter import *
import random

def NouveauLance():
  nb = random.randint(1,6)
  Texte.set('Result -> ' + str(nb))

# creation of the main window
MaFenetre = Tk()
MaFenetre.title('De a 6 faces')
MaFenetre.geometry('300x100+400+400')
 
# creation of a widget Button (Lancer)
BoutonLancer = Button(MaFenetre, text='Lancer',command=NouveauLance)
# positionning the widget with the method pack
BoutonLancer.pack(side=LEFT,padx=5,pady=5)

# creation of a widget Button (Quitter)
BoutonQuitter = Button(MaFenetre, text='Quitter',command=MaFenetre.destroy)
BoutonQuitter.pack(side=LEFT,padx=5,pady=5)

Texte = StringVar()
NouveauLance()

# creation of a widget Label (texte 'result -> x')
LabelResultat = Label(MaFenetre, textvariable = Texte, fg='red', bg='white')
LabelResultat.pack(side=LEFT,padx=5,pady=5)

MaFenetre.mainloop()
