from tkinter import *

class item(Frame):
    def __init__(self, parent, button1, button2):
        barraSuperior = Frame(parent, bg='#222')
        barraSuperior.pack(fill=X, expand='0', anchor=N, ipady=10)
        button = Button(barraSuperior, text=button1, font='Segeo_UI 11', fg='#121212', bg='#18c947', borderwidth=0, cursor='hand2')
        button.pack(anchor=W, fill=Y, expand='1', ipadx=50, side=LEFT, pady=(5, 5), padx=(5, 5))
        lbl : Label = Label(barraSuperior, text='Seletto Contabilidade', font='Segeo_UI 11 bold', bg='#222', fg='#18c947')
        lbl.pack(anchor=CENTER, fill=Y, expand='1', ipadx=10, side=LEFT)
        button = Button(barraSuperior, text=button2, font='Segeo_UI 11', fg='#121212', bg='#18c947', borderwidth=0, cursor='hand2', command=self.on_click)
        button.pack(anchor=E, fill=Y, expand='1', ipadx=50, side=LEFT, pady=(5, 5), padx=(5, 5))
    def on_click(self):
        self['text'] = 'Hi'