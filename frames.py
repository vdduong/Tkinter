# a widget Frame is a rectangular zone that can include other widgets
from Tkinter import *

# creation of the main window
Mafenetre = Tk()
Mafenetre.title('Frame widget')
Mafenetre['bg']='bisque' # background color

# creation of a widget Frame in the main window
Frame1 = Frame(Mafenetre, borderwidth=2,relief=GROOVE)
Frame1.pack(side=LEFT, padx=10,pady=10)

# creation of a second Frame in the main window
Frame2 = Frame(Mafenetre, borderwidth=2,relief=GROOVE)
Frame2.pack(side=LEFT,padx=10,pady=10)

# creation of a widget Frame ... in a widget Frame
# the widget Frame1 is the parent of the Frame3
Frame3 = Frame(Frame1,bg='white',borderwidth=2,relief=GROOVE)
Frame3.pack(side=LEFT,padx=10,pady=10)

# creation of a Label et a Button in the widget Frame
Label(Frame1, text="RDV dentiste samedi a 15h").pack(padx=10,pady=10)
Button(Frame1,text="Effacer",fg='navy',command=Frame1.destroy).pack(padx=10,pady=10)

Label(Frame2,text="Reviser le control d info").pack(padx=10,pady=10)
Button(Frame2, text="Effacer",fg="navy",command=Frame2.destroy).pack(padx=10,pady=10)

Label(Frame3,text="RDV dentiste a 10h").pack(padx=10,pady=10)
Button(Frame3,text="Effacer",fg="navy",command=Frame3.destroy).pack(padx=10,pady=10)

Mafenetre.mainloop()
