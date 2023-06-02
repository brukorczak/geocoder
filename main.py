import requests
import geocoder

API_KEY = "2b4dc6cd6290d850918774e2f84c79c0"

# Obter as coordenadas da localização atual
g = geocoder.ip('me')
latitude, longitude = g.latlng

# Fazer a requisição para a API do OpenWeatherMap usando as coordenadas
link = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}&lang=pt_br"

requisicao = requests.get(link)
requisicao_dic = requisicao.json()
descricao = requisicao_dic['weather'][0]['description']
temperatura = requisicao_dic['main']['temp'] - 273.15

print(descricao, f"{temperatura}ºC")
