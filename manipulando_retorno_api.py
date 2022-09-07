import re
import pandas as pd
from api_2 import *

# Transformando Json em DataFrame
df_jogos_aovivo = pd.DataFrame(retorna_jogos_ao_vivo())

# Percorrendo DataFrame e ajustando retorno/formato dos dados
for index, column in df_jogos_aovivo.iterrows():
    nm_campeonato = column["campeonato"]
    camp          = re.search(r"(nome': )(.*,)", str(nm_campeonato)).group(2).replace("'","").replace(",","")
    df_jogos_aovivo.loc[index, "campeonato"] = str(camp)


df_jogos_aovivo.to_csv(r"C:\Users\didico\Documents\arquivos\teste_dtf.csv", encoding='utf-8', index=False)
#print(df_jogos_aovivo.loc[0, "campeonato"])