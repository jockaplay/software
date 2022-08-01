from tkinter import *
import BarraSuperior
import menu

janela = Tk()
largura = 1280
altura = 720
janelaLargura = janela.winfo_screenwidth()
janelaAltura = janela.winfo_screenheight()
posy = janelaAltura / 2.1 - altura / 2
posx = janelaLargura / 2 - largura / 2
janela.geometry('%dx%d+%d+%d'%(largura, altura, posx, posy))
janela.title('Primeiro programa')
janela.minsize(640, 380)
janela.config(bg='#121212')

BarraSuperior.item(janela, 'Voltar', 'Menu')
menu.item(janela)

janela.mainloop()