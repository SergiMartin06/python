import requests


"""
parametres={"access_key":"9d39e29bff4eb2841c644d72789c3bac",
   		 "symbols":"AENA.BMEX"}
# Fem la petició indicant l'url i els paràmetres
res=requests.get("http://api.marketstack.com/v1/eod",params=parametres)
"""
def consultaapirest():
    superhero_name=input("Ingresa un superheroe: ")
    parametres = {

        "access_key": "https://superheroapi.com/api/access-token/"
        "results-for": superhero_name
        
        }
    #url = "https://superheroapi.com/api/{YOUR_API_KEY}/search/{superhero_name}"
    response = requests.get("https://superheroapi.com/api/",parametres)
    if response.status_code == 200:
        data = response.json()

        if data['response'] == 'success':
            superhero = data['results'][0]
            name = superhero['name']
            powerstats = superhero['powerstats']
            
            print('Nombre:', name)
            print('Estadísticas de poder:')
            for stat, value in powerstats.items():
                print(f"{stat}: {value}")
        else:
            print('Superhéroe no encontrado.')
    else:
        print('Error al acceder a la API:', response.status_code)


consultaapirest()