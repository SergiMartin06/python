import requests

def obtener_chiste_chuck_norris():
    url = "https://api.chucknorris.io/jokes/random"
    respuesta = requests.get(url)
    datos = respuesta.json()
    
    chiste = datos["value"]
    print(chiste)

obtener_chiste_chuck_norris()
