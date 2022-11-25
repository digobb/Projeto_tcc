import re
import pandas as pd
from api import *

def chama_retorno_jogos_aovivo():
    # Transformando Json em DataFrame
    df_jogos_aovivo   = pd.DataFrame(retorna_jogos_ao_vivo())

    # Percorrendo DataFrame e ajustando retorno/formato dos dados
    for pos, column in df_jogos_aovivo.iterrows():
        # campeonato
        nm_campeonato = column["campeonato"]
        camp          = re.search(r"(nome': )(.*,)", str(nm_campeonato)).group(2).replace("'","").replace(",","")
        df_jogos_aovivo.loc[pos, "campeonato"] = str(camp)

        # time mandante
        tm_mandante = column["time_mandante"]
        time_1      = re.search(r"(nome_popular': )(.*?,)", str(tm_mandante)).group(2).replace("'","").replace(",","")
        df_jogos_aovivo.loc[pos, "time_mandante"] = str(time_1)

        # time_visitante
        tm_visitante = column["time_visitante"]
        time_2       = re.search(r"(nome_popular': )(.*?,)", str(tm_visitante)).group(2).replace("'", "").replace(",", "")
        df_jogos_aovivo.loc[pos, "time_visitante"] = str(time_2)

        # estadio
        nm_estadio = column["estadio"]
        estadio    = re.search(r"(nome_popular': )(.*?})", str(nm_estadio)).group(2).replace("'","").replace("}","")
        df_jogos_aovivo.loc[pos, "estadio"] = str(estadio)

        # id da partida
        link_partida = column["_link"]
        link         = str(link_partida).replace("/v1/partidas/", '')
        df_jogos_aovivo.loc[pos, "_link"] = str(link)

        # Apaga caso campeonato não seja COPA DO BRASIL
        if camp != "Copa do Brasil":
            print(f'Apagando... {nm_campeonato}')
            df_jogos_aovivo.drop(index=pos, inplace=True)

    df_jogos_aovivo.to_csv(r"C:/Users/didico/Documents/Projeto_TCC/projeto_tcc/arquivo/jogos_aovivo.csv", encoding='utf-8', index=False)
    return True
    
