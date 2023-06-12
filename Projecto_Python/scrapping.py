import requests
from bs4 import BeautifulSoup

url = 'https://es.wikipedia.org/wiki/Inteligencia_artificial'


response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find('h1', class_='firstHeading').text
    print('Título:', title)
    first_paragraph = soup.find('p').text
    print('Primer párrafo:', first_paragraph)
    links = soup.find_all('a')
    print('Enlaces encontrados:')
    for link in links:
        print(link['href'])
else:
    print('Error al acceder a la página:', response.status_code)
