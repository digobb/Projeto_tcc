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

dados = pd.read_csv(r'C:/Users/didico/Documents/Projeto_TCC/projeto_tcc/arquivo/teste_dtf.csv')
 

def retorna_link_partida(btn):
   print(btn)
   return str(btn)


# Menu
def tela_principal():
    tela = Tk()
    tela.title('Jogos ao vivo do campeonato')
    frame_janela = Frame(tela, width=500, height=250)
    frame_janela.grid()
    for index, column in dados.iterrows():
        id_partida = column['_link']
        dados.loc[0, '_link'] = Button(tela, text=f'{column["time_mandante"]} x {column["time_visitante"]}', font=('', 12), bg='black', fg='white')
        dados.loc[0, '_link']['command'] = lambda btn=id_partida: retorna_link_partida(btn)
        dados.loc[0, '_link'].grid(column=0)

    tela.mainloop()

tela_principal()

