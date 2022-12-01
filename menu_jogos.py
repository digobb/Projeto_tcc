from tkinter import *
from dashboard_estatisticas import grafico_partida as gp
from api import *
from manipulando_retorno_api import chama_retorno_jogos_aovivo
import pandas as pd
import os, time
from datetime import date

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
    tela['background']='white'
    tela.iconbitmap('C:/Users/didico/Documents/Projeto_TCC/projeto_tcc/img/icon.ico')
    tela.title('Jogos ao vivo')
    tela.geometry("400x800") 
    tela.minsize(400, 400)
    tela.resizable(False, False)

    img_logo = PhotoImage(file='C:/Users/didico/Documents/Projeto_TCC/projeto_tcc/img/campeonato_brasileiro.png', width=150, height=150)
    logo     = Label(tela, image=img_logo)
    logo.img_logo = img_logo
    logo.place(x=120, y=3)

    data_atual = date.today()
    data_atual = data_atual.strftime('%d/%m/%Y')

    if os.path.exists('C:/Users/didico/Documents/Projeto_TCC/projeto_tcc/arquivo/jogos_aovivo.csv'):
        print('Arquivo contendo os jogos ao vivo encontrado, verificando...')
        dados = pd.read_csv(f'C:/Users/didico/Documents/Projeto_TCC/projeto_tcc/arquivo/jogos_aovivo.csv')
        if dados.loc[0, 'data_realizacao'] != data_atual:
            print('Atualizando partidas...')
            os.remove('C:/Users/didico/Documents/Projeto_TCC/projeto_tcc/arquivo/jogos_aovivo.csv'), time.sleep(1)
            chama_retorno_jogos_aovivo(), time.sleep(1.5)
            dados = pd.read_csv(f'C:/Users/didico/Documents/Projeto_TCC/projeto_tcc/arquivo/jogos_aovivo.csv')
        else:
            dados = pd.read_csv(f'C:/Users/didico/Documents/Projeto_TCC/projeto_tcc/arquivo/jogos_aovivo.csv')
    else:
        print('Não foi encontrado arquivo com os jogos ao vivo... criando...')
        chama_retorno_jogos_aovivo(), time.sleep(1.5)
        dados = pd.read_csv(f'C:/Users/didico/Documents/Projeto_TCC/projeto_tcc/arquivo/jogos_aovivo.csv')
    
    pos_y = int(135)
    for index, column in dados.iterrows():
        id_partida = column['_link']
        dados.loc[0, '_link'] = Button(tela, text=f'{column["time_mandante"]} x {column["time_visitante"]}', font=('', 12), bg='#305EE4', fg='white')
        dados.loc[0, '_link']['command'] = lambda id=id_partida: dados_partida_id(id)
        pos_y = pos_y + 35
        dados.loc[0, '_link'].place(x=110, y=pos_y)

    tela.mainloop()

tela_principal()

