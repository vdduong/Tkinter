# browser images with the widget Menu
# dialog box with FileDialog to search for files
# the widget Canvas print the image

from Tkinter import *
import tkinter.messagebox
import tkinter.filedialog

def Ouvrir():
  Canevas.delete(ALL) # delete the graphic zone
  filename=tkinter.filedialog.askopenfilename(title="Ouvrir une image",filetypes=[('gif files','.gif'),\
                                                            ('all files','.*')])
  print(filename)
  photo = PhotoImage(file=filename)
  gifdict[filename]=photo # reference
  print(gifdict)
  
  Canevas.create_image(0,0,anchor=NW,image=photo)
  Canevas.config(height=photo.height(),width=photo.width())
  
  Mafenetre.title("Image "+str(photo.width()) + " x " + str(photo.height())

def Fermer():
  Canevas.delete(ALL)
  Mafenetre.title("Image")

def Apropos():
  tkinter.messagebox.showinfo("A propos","Tutorial Python Tkinter")
  
# main window
Mafenetre=Tk()
Mafenetre.title("Image")

# creation of a widget Menu
menubar = Menu(Mafenetre)
menufichier = Menu(menubar,tearoff=0)
menufichier.add_command(label="Ouvrir une image",command=Ouvrir)
menufichier.add_command(label="Fermer l'image",command=Fermer)
menufichier.add_command(label="Quitter",command=Mafenetre.destroy)
menubar.add_cascade(label="Fichier",menu=menufichier)

menuaide = Menu(menubar,tearoff=0)
menuaide.add_command(label="A propos",command=Apropos)
menubar.add_cascade(label="Aide", menu=menuaide)

# showing the menu
Mafenetre.config(menu=menubar)

# creation of the widget Canvas
Canevas = Canvas(Mafenetre)
Canevas.pack(padx=5,pady=5)

# utilisation d un dictionnaire pour conserver une reference
gifdict={}
Mafenetre.mainloop()
