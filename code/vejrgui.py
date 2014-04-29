# VEJR GUI
from vejret import hent_vejr
from Tkinter import *

class App:

	def __init__(self, master):

		frame = Frame(master)
		frame.pack()
		
		self.overskrift = Label(frame, text="VEJR APP")
		self.overskrift.grid(row=0, column=0, columnspan=2)
		self.overskrift.pack()
		
		# Bynavn
		self.bynavn_label = Label(frame, text="Bynavn")
		self.bynavn_label.grid(row=1, column=0)
		self.bynavn_label.pack()
		self.bynavn = Entry(frame, text='Copenhagen')
		self.bynavn.focus_set()
		self.bynavn.grid(row=1, column=1)
		self.bynavn.pack()

		# Landekode
		self.landekode_label = Label(frame, text="Landekode")
		self.landekode_label.grid(row=2, column=0)
		self.landekode_label.pack()
		self.landekode = Entry(frame, text='dk')
		self.landekode.grid(row=2, column=1)
		self.landekode.pack()
		
		# Resultat
		self.result_text = StringVar()
		self.resultat = Label(frame, textvariable=self.result_text)
		self.resultat.grid(row=3, column=0, columnspan=2)
		self.resultat.pack()
		self.result_text.set('Enter cityname and country code')
		
		# Knapper
		self.hent_vejr_knap = Button(
			frame, text="Hent vejr", command=self.do_hent_vejr)
		self.hent_vejr_knap.grid(row=4,column=0)
		self.hent_vejr_knap.pack()

		self.quit_knap = Button(
			frame, text="QUIT", fg="red", command=frame.quit)
		self.quit_knap.grid(row=4, column=0)
		self.quit_knap.pack()

	def do_hent_vejr(self):
		bynavn = self.bynavn.get()
		landekode = self.landekode.get()
		self.result_text.set('Henter vejr...')
		vejr = hent_vejr(bynavn, landekode)
		self.result_text.set(vejr)
		
root = Tk()

app = App(root)

root.mainloop()
root.destroy() # optional; see description below