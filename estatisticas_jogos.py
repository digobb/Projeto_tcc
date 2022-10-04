import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

## TESTE USO MATPLOTLIB ##


dados = pd.read_csv(r'C:/Users/didico/Documents/arquivos/teste_dtf.csv')

x = [dados.loc[0, "time_mandante"], dados.loc[0, "time_visitante"]]
y = [2,6]

#plt.plot(x, y, "r--")
plt.barh(x, y, align='center', alpha=1)

plt.title("CHUTES A GOL", fontdict={'family': 'Consolas', 'color' : 'black','weight': 'bold','size': 16},loc='center')


plt.xlabel('Linguagens de programação')
#plt.ylabel('Pontuações')

plt.show()