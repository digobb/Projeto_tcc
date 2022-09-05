import requests

url = "https://livescore-football.p.rapidapi.com/soccer"

headers = {
	"X-RapidAPI-Key": "fc0036384cmsh0fd566e2293b5bap1fc36ajsnf41c84bc83bd",
	"X-RapidAPI-Host": "livescore-football.p.rapidapi.com"
}

def retorna_code_countries():
	codes_countries = f'{url}/countries'
	response       = requests.request("GET", codes_countries, headers=headers)
	print(response.text)
	return response

def retorna_ligas():
	leagues     = f'{url}/leagues-by-country'
	querystring = {"country_code": "brazil"}
	response    = requests.request("GET", leagues, headers=headers, params=querystring)
	print(response.text)
	return response

def dados_campeonato_brasileiro():
	campeonato_brasileiro = f'{url}/matches-by-league'
	querystring           = {"country_code": "brazil", "league_code": "brasileiro-u20-group-a", "timezone_utc": "0:00"}
	response 			  = requests.request("GET", campeonato_brasileiro, headers=headers, params=querystring)
	print(response.text)
	return response

def partidas_do_dia():
	partidas_dia = f'{url}/matches-by-date'
	querystring = {"date":"20201017","league_code":"premier-league","timezone_utc":"0:00","country_code":"england"}
	response     = requests.request("GET", partidas_dia, headers=headers, params=querystring)
	print(response.text)
	return response

partidas_do_dia()