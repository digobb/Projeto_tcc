from distutils.cmd import Command
from sqlite3 import Row
from tkinter import *
from tkinter import ttk
from turtle import position
from PIL import Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from dashboard_estatisticas import grafico_partida as gp
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dados = pd.read_csv(r'C:/Users/didico/Documents/arquivos/teste_dtf.csv')

def clicar(btn):
   print(btn)

# Menu
def tela_principal():
    tela = Tk()
    tela.title('Jogos ao vivo do campeonato')
    frame_janela = Frame(tela, width=500, height=250)
    frame_janela.grid()
    for index, column in dados.iterrows():
        id_partida = column['_link']
        #dados.loc[0, '_link'] = Button(frame_janela, text=f'{column["time_mandante"]} x {column["time_visitante"]}', command=gp)
        dados.loc[0, '_link'] = Button(tela, text=f'{column["time_mandante"]} x {column["time_visitante"]}', font=('', 12), bg='black', fg='white')
        dados.loc[0, '_link']['command'] = lambda btn=id_partida: clicar(btn)
        dados.loc[0, '_link'].grid(column=0)

    '''btn = Button(tela,text="Fatos",font=("",20),bg="black",fg="white")
    btn["command"] = lambda btn=btn: clicar(btn)
    btn.grid(row=1,column=1)

    btn = Button(tela,text="boatos",font=("",20),bg="black",fg="white",command=clicar)
    btn["command"] = lambda btn=btn: clicar(btn)
    btn.grid(row=2,column=1)'''

    tela.mainloop()

tela_principal()

