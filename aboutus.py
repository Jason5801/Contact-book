from tkinter import *

class About(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("550x550+550+200")
        self.title("About Us")
        self.resizable(False, False)

        self.top = Frame(self, height=550, width=550, bg='orange')
        self.top.pack(fill=BOTH)

        self.text = Label(self.top, text='Hey This is about us page'
                          '\n this application is made for educational purpose',
                          font = 'arial 14 bold', bg="orange", fg = "white"
                          )

        self.text.place(x=50, y=50)