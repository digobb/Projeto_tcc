from asyncore import read
from distutils.cmd import Command
from tkinter import *
from tkinter import ttk
from turtle import position
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import re
import json

#dados = pd.read_csv(r'C:/Users/didico/Documents/Projeto_TCC/projeto_tcc/arquivo/teste_dtf.csv')
    
def grafico_partida(id_partida):

    # VERIFICA SE ARQUIVO CONTENDO OS DADOS DA PARTIDA EXISTEM.
    if os.path.exists(f'C:/Users/didico/Documents/Projeto_TCC/projeto_tcc/arquivo/dados_partida_{id_partida}.csv'):
        print('Arquivo com dados da partida encontrados!')
        dados = pd.read_csv(f'C:/Users/didico/Documents/Projeto_TCC/projeto_tcc/arquivo/dados_partida_{id_partida}.csv')
    else:
        print('Nao foi encontrado arquivo com dados da partida')
    
    ################# cores ###############
    co0 = "#f0f3f5"  # Preta
    co1 = "#feffff"  # branca
    co2 = "#6f9fbd"  # azul
    co3 = "#38576b"  # valor
    co4 = "#403d3d"  # para letra
    co5 = "#e06636"   
    co6 = "#6dd695" 

    fundo = "#3F729B"

    janela = Tk()
    janela.iconbitmap('C:/Users/didico/Documents/Projeto_TCC/projeto_tcc/img/icon.ico')
    janela['background']='white'
    #janela.state('zoomed')
    janela.title(f'Estatisticas: {dados.loc[0, "time_mandante.nome_popular"]} x {dados.loc[0, "time_visitante.nome_popular"]}')

    ################# Frames ####################
    # Neste frame iremos Mostrar o nome do Aplicativo
    frame_app_nome = Frame(janela, width=1370, height=40, pady=0,padx=0, bg=co1,  relief="flat")
    frame_app_nome.grid(row=0, column=0)

    #Aqui iremos mostrar as estatisticas
    frame_quadros = Frame(janela, width=1370, height=1000,bg=co0, pady=15, padx=7, relief="flat",)
    frame_quadros.grid(row=1, column=0, sticky=NW)

    ################# Criando label para o frame_app_nome #############
    app_nome = Label(frame_app_nome, text=f"{dados.loc[0, 'time_mandante.nome_popular']} {dados.loc[0, 'placar_mandante']} X {dados.loc[0, 'placar_visitante']} {dados.loc[0,'time_visitante.nome_popular']}", width=30, height=2,pady=1, padx=0, relief="flat", anchor=N, font=('Ivy 14 bold'), bg=co1, fg=co4)
    app_nome.place(x=500, y=5)

    #------------------------------------------------------------------------------------------------------
    # CAMPEONATO
    frame_campeonato = Frame(frame_quadros, width=200, height=90,bg=co1, relief="flat")
    frame_campeonato.place(x=0, y=0)

    app_camp = Label(frame_campeonato, text="", width=1, height=10,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 1 bold'), bg=co2, fg=co4)
    app_camp.place(x=0, y=0)

    app_nome_camp = Label(frame_campeonato, text="CAMPEONATO", height=1, pady=0,padx=0, relief="flat", anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co4)
    app_nome_camp.place(x=20, y=5)

    app_camp = Label(frame_campeonato, text=f"{dados.loc[0, 'campeonato.nome_popular']}", height=1, pady=0, padx=0,relief="flat", anchor=CENTER, font=('Ivy 11 bold'), bg=co1, fg=co3)
    app_camp.place(x=40, y=35)

    app_nome_rodada = Label(frame_campeonato, text=f"{dados.loc[0, 'rodada']}", height=1, pady=0,padx=0, relief="flat", anchor=CENTER, font=('Ivy 8 bold'), bg=co1, fg=co6)
    app_nome_rodada.place(x=60, y=70)

    #------------------------------------------------------------------------------------------------------
    # Cartoes
    frame_cartoes = Frame(frame_quadros, width=200, height=160,bg=co1, relief="flat")
    frame_cartoes.place(x=210, y=0)

    app_pr = Label(frame_cartoes, text="", width=1, height=10,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 1 bold'), bg=co2, fg=co4)
    app_pr.place(x=0, y=0)

    app_nome_rev = Label(frame_cartoes, text="CARTÕES", height=1,pady=0, padx=0, relief="flat", anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co4)
    app_nome_rev.place(x=20, y=5)

    cart_amarelo_mandante   = str(dados.loc[0, 'cartoes.amarelo.mandante'])
    cart_vermelho_mandante  = str(dados.loc[0, 'cartoes.vermelho.mandante'])
    cart_amarelo_visitante  = str(dados.loc[0, 'cartoes.amarelo.visitante'])
    cart_vermelho_visitante = str(dados.loc[0, 'cartoes.vermelho.visitante'])
    # time mandante
    app_nome_va = Label(frame_cartoes, text=f"{dados.loc[0, 'time_mandante.nome_popular']}", height=1, pady=0,padx=0, relief="flat", anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co3)
    app_nome_va.place(x=20, y=35)
    cart_amarelo_1 = Label(frame_cartoes, text=" ", height=1, width=1, pady=0,padx=0, relief="flat", anchor=CENTER, font=('Ivy 10 bold'), bg="yellow")
    cart_amarelo_1.place(x=30, y=60)
    qtd_cartao_amr1 = Label(frame_cartoes, text=f"{cart_amarelo_mandante.count('cartao_id')}", height=1, pady=0,padx=0, relief="flat", anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co3)
    qtd_cartao_amr1.place(x=45, y=60)
    cart_vermelho_1 = Label(frame_cartoes, text=" ", height=1, width=1, pady=0,padx=0, relief="flat", anchor=CENTER, font=('Ivy 10 bold'), bg="red")
    cart_vermelho_1.place(x=90, y=60)
    qtd_cartao_verm1 = Label(frame_cartoes, text=f"{cart_vermelho_mandante.count('cartao_id')}", height=1, pady=0,padx=0, relief="flat", anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co3)
    qtd_cartao_verm1.place(x=105, y=60)
    # time visitante
    app_nome_va = Label(frame_cartoes, text=f"{dados.loc[0, 'time_visitante.nome_popular']}", height=1, pady=0,padx=0, relief="flat", anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co3)
    app_nome_va.place(x=20, y=90)
    cart_amarelo_2 = Label(frame_cartoes, text=" ", height=1, width=1, pady=0,padx=0, relief="flat", anchor=CENTER, font=('Ivy 10 bold'), bg="yellow")
    cart_amarelo_2.place(x=30, y=115)
    qtd_cartao_amr_2 = Label(frame_cartoes, text=f"{cart_amarelo_visitante.count('cartao_id')}", height=1, pady=0,padx=0, relief="flat", anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co3)
    qtd_cartao_amr_2.place(x=45, y=115)
    cart_vermelho_2 = Label(frame_cartoes, text=" ", height=1, width=1, pady=0,padx=0, relief="flat", anchor=CENTER, font=('Ivy 10 bold'), bg="red")
    cart_vermelho_2.place(x=90, y=115)
    qtd_cartao_verm_2 = Label(frame_cartoes, text=f"{cart_vermelho_visitante.count('cartao_id')}", height=1, pady=0,padx=0, relief="flat", anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co3)
    qtd_cartao_verm_2.place(x=105, y=115)

    # ------------------------------------------------------------------------------------------------------
    # Escalacao
    # TIME MANDANTE
    esc_mand_tit_json = str(dados.loc[0, 'escalacoes.mandante.titulares']).replace('\'', '"')
    esc_mand_tit      = json.loads(esc_mand_tit_json)

    frame_escalacao = Frame(frame_quadros, width=410, height=400,bg=co1, relief="flat")
    frame_escalacao.place(x=0, y=175)

    app_esc = Label(frame_escalacao, text="", width=1, height=10,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 1 bold'), bg=co2, fg=co4)
    app_esc.place(x=0, y=0)

    app_nome_esc = Label(frame_escalacao, text="ESCALAÇÕES", height=1,pady=0, padx=0, relief="flat", anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co4)
    app_nome_esc.place(x=20, y=5)

    sigla_time_mand = Label(frame_escalacao, text=f"{dados.loc[0, 'time_mandante.sigla']}", height=1, pady=0,padx=0, relief="flat", anchor=CENTER, font=('Ivy 13 bold'), bg=co1, fg=co3)
    sigla_time_mand.place(x=67, y=40)

    sigla_time_vis = Label(frame_escalacao, text=f"{dados.loc[0, 'time_visitante.sigla']}", height=1, pady=0,padx=0, relief="flat", anchor=CENTER, font=('Ivy 13 bold'), bg=co1, fg=co3)
    sigla_time_vis.place(x=270, y=40)

    y = int(50)
    for jogador in range(11):
        # Numero camisa titular mandate
        cam_tit          = esc_mand_tit[jogador]['camisa']
        cam_tit_mandante = Label(frame_escalacao, text=f"{cam_tit}", height=1,pady=1, padx=0, relief="flat", anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co4)
        # Nome jogador titular mandante
        nm_tit           = esc_mand_tit[jogador]['atleta']['nome_popular']
        nm_tit_mandate   = Label(frame_escalacao, text=f"{nm_tit}", height=1,pady=1, padx=0, relief="flat", anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co4)
        # Sigla posicao dos jogadores titulares time mandante.
        sg_tit          = esc_mand_tit[jogador]['posicao']['sigla']
        sg_tit_mandante = Label(frame_escalacao, text=f"{sg_tit}", height=1,pady=1, padx=0, relief="flat", anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co4)

        y = y + 25
        if cam_tit_mandante:
            cam_tit_mandante.place(x=5, y=y)
        if nm_tit_mandate:
            nm_tit_mandate.place(x=25, y=y)
        if sg_tit_mandante:
            sg_tit_mandante.place(x=155, y=y)
        
    # TIME VISITANTE
    esc_mand_vis_json = str(dados.loc[0, 'escalacoes.visitante.titulares']).replace('\'', '"')
    esc_vis_tit       = json.loads(esc_mand_vis_json)

    y = int(50)
    for jogador_vis in range(11):
        # Numero camisa titular visitante
        cam_vis           = esc_vis_tit[jogador_vis]['camisa']
        cam_tit_visitante = Label(frame_escalacao, text=f"{cam_vis}", height=1,pady=1, padx=0, relief="flat", anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co4)
        # Nome jogador titular visitante
        nm_vis           = esc_vis_tit[jogador_vis]['atleta']['nome_popular']
        nm_tit_visitante = Label(frame_escalacao, text=f"{nm_vis}", height=1,pady=1, padx=0, relief="flat", anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co4)
        # Sigla posicao dos jogadores visitante
        sg_vis           = esc_vis_tit[jogador_vis]['posicao']['sigla']
        sg_tit_visitante = Label(frame_escalacao, text=f"{sg_vis}", height=1,pady=1, padx=0, relief="flat", anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co4)

        y = y + 25
        if cam_tit_visitante:
            cam_tit_visitante.place(x=380, y=y)
        if nm_tit_visitante:
            nm_tit_visitante.place(x=270, y=y)
        if sg_tit_visitante:
            sg_tit_visitante.place(x=230, y=y)

    # ------------------------------------------------------------------------------------------------------
    # Posse de bola
    frame_possebola = Frame(frame_quadros, width=500, height=200, bg=co1, relief="flat")
    frame_possebola.place(x=420, y=0)

    posse_bola_mandante  = str(dados.loc[0, 'estatisticas.mandante.posse_de_bola']).replace('%','')
    posse_bola_visitante = str(dados.loc[0, 'estatisticas.visitante.posse_de_bola']).replace('%','')

    times           = [f"{dados.loc[0,'time_mandante.nome_popular']}", f"{dados.loc[0, 'time_visitante.nome_popular']}"]
    vlr_posses_bola = [int(posse_bola_mandante), int(posse_bola_visitante)]
    
    figura = plt.Figure(figsize=(11, 2), dpi=93)
    canva  = FigureCanvasTkAgg(figura, frame_possebola)
    canva.get_tk_widget().grid(row=1, column=0, sticky=NSEW)
    
    ax = figura.add_subplot()
    a = ax.barh(times, vlr_posses_bola)
    ax.bar_label(a, fmt='%1.1f%%')

    app_pr = Label(frame_possebola, text="", width=1, height=10, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 1 bold'), bg=co2, fg=co4)
    app_pr.place(x=0, y=0)
    app_nome_rev = Label(frame_possebola, text="POSSE DE BOLA", height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
    app_nome_rev.grid(row=0, column=0, padx=20, pady=0, sticky=NSEW)
    
    # ------------------------------------------------------------------------------------------------------
    # POSSE DE BOLA

    frame_poss_bola = Frame(frame_quadros, width=200,height=200, bg=co1, relief="flat",)
    frame_poss_bola.place(x=420, y=230)

    # faça figura e atribua objetos de eixo
    figura = plt.Figure(figsize=(5.15, 4), dpi=80)
    ax = figura.add_subplot(111)

    mand_posse_bola = str(dados.loc[0, 'estatisticas.mandante.posse_de_bola']).replace('%','')
    visi_posse_bola = str(dados.loc[0, 'estatisticas.visitante.posse_de_bola']).replace('%','')

    # posse
    posse_bola = [int(mand_posse_bola), int(visi_posse_bola)]

    # times
    times_posse_bola = [str(dados.loc[0, 'time_mandante.nome_popular']), str(dados.loc[0, 'time_visitante.nome_popular'])]

    # only "explode
    explode = (0.03, 0.03)

    # colors = ['#665191', '#a05195','#d45087',  "#f95d6a", "#ff7c43", "#ffa600"]
    colors = ['#ff9999',  '#c5cae9']


    ax.pie(posse_bola, explode=explode, wedgeprops=dict(width=0.64), labels=times_posse_bola, colors=colors, autopct='%1.1f%%', shadow=True, startangle=95)

    app_poss = Label(frame_poss_bola, text="", width=1, height=10, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 1 bold'), bg=co2, fg=co4)
    app_poss.place(x=0, y=0)
    app_posse = Label(frame_poss_bola, text="POSSE DE BOLA", height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
    app_posse.grid(row=0, column=0, pady=0, padx=20, columnspan=2, sticky=NSEW)
    canva_posse = FigureCanvasTkAgg(figura, frame_poss_bola)
    canva_posse.get_tk_widget().grid(row=1, column=0, sticky=NSEW)


    # ------------------------------------------------------------------------------------------------------
    # EXEMPLOS GRAF BAR
    # Faturamento por Vendedores 

    frame_fin_precisao = Frame(frame_quadros, width=200, height=200,bg=co1, relief="flat",)
    frame_fin_precisao.place(x=840, y=230)

    # faça figura e atribua objetos de eixo
    figura = plt.Figure(figsize=(7.3, 4.6), dpi=70)
    ax = figura.add_subplot(111)

    mand_finalizacao_precisao = str(dados.loc[0, 'estatisticas.mandante.finalizacao.precisao']).replace('%','')
    vis_finalizacao_precisao = str(dados.loc[0, 'estatisticas.visitante.finalizacao.precisao']).replace('%','')

    # Finalizacoes
    finalizacao_total = [int(mand_finalizacao_precisao), int(vis_finalizacao_precisao)]


    # times
    times_finzalicao = [str(dados.loc[0, 'time_mandante.nome_popular']), str(dados.loc[0, 'time_visitante.nome_popular'])]

    ax.bar(times_finzalicao, finalizacao_total,  color=colors, width=0.8)

    # create a list to collect the plt.patches data
    totals = []

    c = 0
    # set individual bar lables using above list
    for i in ax.patches:
        # get_x pulls left or right; get_height pushes up or down
        ax.text(i.get_x()-.03, i.get_height()+.05, str(finalizacao_total[c])+'%', fontsize=12, fontstyle='italic', color='dimgrey', weight='bold', verticalalignment='baseline',)
        c += 1

    ax.patch.set_facecolor('#FFFFFF')
    ax.spines['bottom'].set_color('#CCCCCC')
    ax.spines['bottom'].set_linewidth(1)
    ax.spines['right'].set_linewidth(0)
    ax.spines['top'].set_linewidth(0)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['left'].set_linewidth(1)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_color('#DDDDDD')
    ax.tick_params(bottom=False, left=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(True, color='#EEEEEE')
    ax.xaxis.grid(False)


    app_prec = Label(frame_fin_precisao, text="", width=1, height=10, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 1 bold'), bg=co2, fg=co4)
    app_prec.place(x=0, y=0)
    app_name_preci = Label(frame_fin_precisao, text="PRECISÃO EM FINALIZAÇÕES", height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
    app_name_preci.grid(row=0, column=0, pady=0, padx=20, columnspan=2, sticky=NSEW)
    canva_prec = FigureCanvasTkAgg(figura, frame_fin_precisao)
    canva_prec.get_tk_widget().grid(row=1, column=0, sticky=NSEW)

    # ------------------------------------------------------------------------------------------------------
    # Escanteios
    frame_escanteio = Frame(frame_quadros, width=200,height=180, bg=co1, relief="flat",)
    frame_escanteio.place(x=420, y=580)

    app_esc = Label(frame_escanteio, text="", width=1, height=10,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 1 bold'), bg=co2, fg=co4)
    app_esc.place(x=0, y=0)

    app_nome_esc = Label(frame_escanteio, text="ESCANTEIOS", height=1, pady=0,padx=0, relief="flat", anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co4)
    app_nome_esc.place(x=20, y=5)

    app_tim1_esc = Label(frame_escanteio, text=f"{dados.loc[0, 'time_mandante.nome_popular']}", height=1, pady=0,padx=0, relief="flat", anchor=CENTER, font=('Ivy 11 bold'), bg=co1, fg='black')
    app_tim1_esc.place(x=20, y=35)
    qtd_esc_mandante = Label(frame_escanteio, text=f"{dados.loc[0, 'estatisticas.mandante.escanteios']} 🚩", height=1, pady=0,padx=0, relief="flat", anchor=CENTER, font=('Ivy 11 bold'), bg=co1, fg=co3)
    qtd_esc_mandante.place(x=45, y=60)

    app_tim2_esc = Label(frame_escanteio, text=f"{dados.loc[0, 'time_visitante.nome_popular']}", height=1, pady=0,padx=0, relief="flat", anchor=CENTER, font=('Ivy 11 bold'), bg=co1, fg='black')
    app_tim2_esc.place(x=20, y=90)
    qtd_esc_visitante = Label(frame_escanteio, text=f"{dados.loc[0, 'estatisticas.visitante.escanteios']} 🚩", height=1, pady=0,padx=0, relief="flat", anchor=CENTER, font=('Ivy 11 bold'), bg=co1, fg=co3)
    qtd_esc_visitante.place(x=45, y=115)

    # ------------------------------------------------------------------------------------------------------
    # OUTRO FRAME

    frame_ex1 = Frame(frame_quadros, width=200,height=180, bg=co1, relief="flat",)
    frame_ex1.place(x=630, y=580)

    app_ex1 = Label(frame_ex1, text="", width=1, height=10,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 1 bold'), bg=co2, fg=co4)
    app_ex1.place(x=0, y=0)

    app_nome_ex1 = Label(frame_ex1, text="FRAME 1", height=1, pady=0,padx=0, relief="flat", anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co4)
    app_nome_ex1.place(x=20, y=5)

    # ------------------------------------------------------------------------------------------------------
    # OUTRO FRAME

    frame_ex2 = Frame(frame_quadros, width=200,height=180, bg=co1, relief="flat",)
    frame_ex2.place(x=840, y=580)

    app_ex2 = Label(frame_ex2, text="", width=1, height=10,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 1 bold'), bg=co2, fg=co4)
    app_ex2.place(x=0, y=0)

    app_nome_ex2 = Label(frame_ex2, text="FRAME 2", height=1, pady=0,padx=0, relief="flat", anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co4)
    app_nome_ex2.place(x=20, y=5)

    # ------------------------------------------------------------------------------------------------------
    # OUTRO FRAME

    frame_ex3 = Frame(frame_quadros, width=200,height=180, bg=co1, relief="flat",)
    frame_ex3.place(x=1050, y=580)

    app_ex3 = Label(frame_ex3, text="", width=1, height=10,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 1 bold'), bg=co2, fg=co4)
    app_ex3.place(x=0, y=0)

    app_nome_ex3 = Label(frame_ex3, text="FRAME 3", height=1, pady=0,padx=0, relief="flat", anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co4)
    app_nome_ex3.place(x=20, y=5)



    janela.mainloop()

