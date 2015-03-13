# interface
import Tkinter
import tkMessageBox
import tkFileDialog
import os

class ButtonNewWindowTOCSY(Tkinter.Frame):
	def __init__(self,*args,**kwargs):
		Tkinter.Frame.__init__(self,*args,**kwargs)
		button = Tkinter.Button(self, text="Open new assignment TOCSY",command=self.new_window)
		button.pack(side="top")
	
	def new_window(self):
		def OpenTOCSY():
			MyTextTOCSYpeaklist.delete(1.0,"end")
			filenameTOCSYpeaklist = tkFileDialog.askopenfilename(title="Open TOCSY peak list", \
					filetypes=[('text files','.peaks'),('all files','*')])
			MyTextTOCSYpeaklist.insert(0.0,filenameTOCSYpeaklist)
			MyTextTOCSYpeaklist.pack(expand=1,fill="both")
			MyTextTOCSYresult.delete(1.0,"end")
			TOCSYpeaklist = filenameTOCSYpeaklist
			f = open(str(os.getcwd())+'/dumpTOCSY.txt','w')
			f.write(filenameTOCSYpeaklist)
			f.close()
		
		def AssignTOCSY():
			pass
	
		window = Tkinter.Toplevel(self)
		FrameTOCSY = Tkinter.Frame(window, borderwidth=2,relief="groove")
		FrameTOCSY.pack(side="left",padx=10,pady=10)
		LabelTOCSY = Tkinter.Label(FrameTOCSY, text="TOCSY peak list automated assignment")
		LabelTOCSY.pack(side="top")
		
		MyTextTOCSYpeaklist = Tkinter.Text(FrameTOCSY)
		MyTextTOCSYpeaklist["bg"] = "black"
		MyTextTOCSYpeaklist["fg"] = "white"
		MyTextTOCSYpeaklist.pack(side="top")
		
		MyTextTOCSYresult = Tkinter.Text(FrameTOCSY, height=3)
		MyTextTOCSYresult.pack()
		
		ButtonOpenTOCSY = Tkinter.Button(FrameTOCSY, text="Open TOCSY peak list",command=OpenTOCSY)
		ButtonAssignTOCSY = Tkinter.Button(FrameTOCSY, text="Assign TOCSY peak list",command=AssignTOCSY)
		ButtonCloseTOCSY = Tkinter.Button(FrameTOCSY, text="Exit", command=window.destroy)
		ButtonOpenTOCSY.pack(side="left")
		ButtonAssignTOCSY.pack(side="left")
		ButtonCloseTOCSY.pack(side="left")
		
		
		
		

class ButtonNewWindowHSQC(Tkinter.Frame):
	def __init__(self,*args,**kwargs):
		Tkinter.Frame.__init__(self,*args,**kwargs)
		button = Tkinter.Button(self, text="Open new assignment HSQC", command=self.new_window)
		button.pack(side="top")
	
	def new_window(self):
		def OpenHSQC():
			MyTextHSQCpeaklist.delete(1.0,"end")
			filenameHSQCpeaklist = tkFileDialog.askopenfilename(title="Open HSQCpeak list", \
					filetypes=[('text files','.peaks'),('all files','*')])
			MyTextHSQCpeaklist.insert(0.0,filenameHSQCpeaklist)
			MyTextHSQCpeaklist.pack(expand=1,fill="both")
			MyTextHSQCresult.delete(1.0,"end")
		
		def AssignHSQC():
			pass
						
		window = Tkinter.Toplevel(self)
		FrameHSQC = Tkinter.Frame(window, borderwidth=2,relief="groove")
		FrameHSQC.pack(side="left",padx=10,pady=10)
		LabelHSQC= Tkinter.Label(FrameHSQC, text="HSQC peak list automated assignment")
		LabelHSQC.pack(side="top")
		
		MyTextHSQCpeaklist = Tkinter.Text(FrameHSQC)
		MyTextHSQCpeaklist["bg"] = "black"
		MyTextHSQCpeaklist["fg"] = "white"
		MyTextHSQCpeaklist.pack(side="top")
		
		MyTextHSQCresult = Tkinter.Text(FrameHSQC, height=3)
		MyTextHSQCresult.pack()
		
		ButtonOpenHSQC = Tkinter.Button(FrameHSQC, text="Open HSQC peak list",command=OpenHSQC)
		ButtonAssignHSQC = Tkinter.Button(FrameHSQC, text="Assign HSQC peak list",command=AssignHSQC)
		ButtonCloseHSQC = Tkinter.Button(FrameHSQC, text="Exit", command=window.destroy)
		ButtonOpenHSQC.pack(side="left")
		ButtonAssignHSQC.pack(side="left")
		ButtonCloseHSQC.pack(side="left")

		
MyMainWindow = Tkinter.Tk()
MyMainWindow.title('ITERAMETA')

Introduction = Tkinter.Label(MyMainWindow, text="ITERAMETA -  an automated assignment program for metabolomics")
Introduction.pack(side="top",padx=50,pady=50)

ButtonSelectTOCSY = ButtonNewWindowTOCSY(MyMainWindow)
ButtonSelectTOCSY.pack(side="bottom",fill="both",expand=True)

ButtonSelectHSQC = ButtonNewWindowHSQC(MyMainWindow)
ButtonSelectHSQC.pack(side="bottom",fill="both",expand=True)

MyMainWindow.mainloop()
