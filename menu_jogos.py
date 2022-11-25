from distutils.cmd import Command
from sqlite3 import Row
from tkinter import *
from tkinter import ttk
from turtle import position
from PIL import Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from dashboard_estatisticas import grafico_partida as gp
from api import *
from manipulando_retorno_api import chama_retorno_jogos_aovivo
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os, time

#dados = pd.read_csv(r'C:/Users/didico/Documents/Projeto_TCC/projeto_tcc/arquivo/teste_dtf.csv')

def dados_partida_id(id):
    print(id)
    dados = retorna_dados_partida(id_partida=id)
    df_dados_partida = pd.json_normalize(dados)
    df_dados_partida.to_csv(f"C:/Users/didico/Documents/Projeto_TCC/projeto_tcc/arquivo/dados_partida_{id}.csv", encoding='utf-8')
    gp(id_partida=id)
    return True

# Menu
def tela_principal():
    tela = Tk()
    tela.title('Jogos ao vivo do campeonato')
    frame_janela = Frame(tela, width=300, height=250)
    frame_janela.grid(padx=2, pady=2)
    if os.path.exists(f'C:/Users/didico/Documents/Projeto_TCC/projeto_tcc/arquivo/jogos_aovivo.csv'):
        print('Arquivo com dados da partida encontrados!')
        dados = pd.read_csv(f'C:/Users/didico/Documents/Projeto_TCC/projeto_tcc/arquivo/jogos_aovivo.csv')
    else:
        print('Nao foi encontrado arquivo com os jogos ao vivo... criando...')
        chama_retorno_jogos_aovivo()
        time.sleep(2)
        dados = pd.read_csv(f'C:/Users/didico/Documents/Projeto_TCC/projeto_tcc/arquivo/jogos_aovivo.csv')
        
    for index, column in dados.iterrows():
        id_partida = column['_link']
        dados.loc[0, '_link'] = Button(tela, text=f'{column["time_mandante"]} x {column["time_visitante"]}', font=('', 12), bg='black', fg='white')
        dados.loc[0, '_link']['command'] = lambda id=id_partida: dados_partida_id(id)
        dados.loc[0, '_link'].grid(column=0)

    tela.mainloop()

tela_principal()

