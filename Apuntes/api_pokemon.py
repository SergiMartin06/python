import requests
for i in range(10):
	a = "https://pokeapi.co/api/v2/evolution-chain/"+str((i+1))
	res=requests.get(a)
	if res.status_code == 200:
    	dades = res.json()
    	print("El nom del pokémon és: {}".format(dades["chain"]["species"]["name"]))
    	for e in dades["chain"]["evolves_to"]:
        	print("Nom de la seva evolució: ", e["species"]["name"])
else:
	print("No hi ha dades.")
