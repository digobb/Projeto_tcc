import requests
from requests.structures import CaseInsensitiveDict

url                      = "https://api.api-futebol.com.br/v1"
headers                  = CaseInsensitiveDict()
headers["Accept"]        = "application/json"
headers["Authorization"] = "Bearer test_5ad63cd33369753b1cb8a002e02180"

# DADOS CAMPEONATO BRASILEIRAO
def retorna_campeonatos():
    url_api     = f'{url}/campeonatos'
    response    = requests.request("GET", url_api, headers=headers)
    status      = requests.get(url_api, headers=headers)
    print(f'---------------------- status: {status} ----------------------')
    print(response.json())
    return response

def retorna_campeonato_brasileiro():
    url_api  = f'{url}/campeonatos/10'
    response = requests.request("GET", url_api, headers=headers)
    status   = requests.get(url_api, headers=headers)
    print(f'---------------------- status: {status} ----------------------')
    print(response.json())
    return response

def retorna_tabela_campeonato_brasileiro():
    url_api  = f'{url}/campeonatos/10/tabela'
    response = requests.request("GET", url_api, headers=headers)
    status   = requests.get(url_api, headers=headers)
    print(f'---------------------- status: {status} ----------------------')
    print(response.json())
    return response

def retorna_artilheiros_campeonato_brasileiro():
    url_api  = f'{url}/campeonatos/10/artilharia'
    response = requests.request("GET", url_api, headers=headers)
    status   = requests.get(url_api, headers=headers)
    print(f'---------------------- status: {status} ----------------------')
    print(response.json())
    return response

def retorna_rodada_atual_campeonato_brasileiro():
    url_api  = f'{url}/campeonatos/10/rodadas/25'
    response = requests.request("GET", url_api, headers=headers)
    status   = requests.get(url_api, headers=headers)
    print(f'---------------------- status: {status} ----------------------')
    print(response.json())
    return response

# DADOS PARTIDAS
def retorna_partidas():
    url_api  = f'{url}/campeonatos/10/partidas'
    response = requests.request("GET", url_api, headers=headers)
    status   = requests.get(url_api, headers=headers)
    print(f'---------------------- status: {status} ----------------------')
    print(response.json())
    return response.json()

def retorna_jogos_ao_vivo():
    url_api  = f'{url}/ao-vivo'
    response = requests.request("GET", url_api, headers=headers)
    status   = requests.get(url_api, headers=headers)
    print(f'---------------------- status: {status} ----------------------')
    print(response.json())
    return response.json()
