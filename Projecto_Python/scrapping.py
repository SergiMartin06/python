import requests

# Definir el nombre del superhéroe
nombre_superheroe = "spider-man"

# Construir la URL de la API con el nombre del superhéroe
url = f"https://superheroapi.com/api/your-api-key/search/{nombre_superheroe}"

# Realizar la solicitud GET a la API
response = requests.get(url)

# Verificar el estado de la respuesta
if response.status_code == 200:
    # Obtener el resultado de la respuesta en formato JSON
    data = response.json()

    # Verificar si se encontró el superhéroe
    if data['response'] == 'success':
        # Obtener información sobre el primer resultado del superhéroe
        superhero = data['results'][0]
        
        # Obtener el nombre, la biografía y las habilidades del superhéroe
        nombre = superhero['name']
        biografia = superhero['biography']
        habilidades = superhero['powerstats']
        
        # Imprimir la información del superhéroe
        print("Nombre:", nombre)
        print("Biografía:", biografia)
        print("Habilidades:", habilidades)
    else:
        print("Superhéroe no encontrado.")
else:
    print("Error al acceder a la API:", response.status_code)
