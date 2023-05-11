# Obtenir l'any actual
from datetime import date
any_actual = date.today().year

# Dades de les persones
persones = [
    {"nom": "Persona 1", "any_naixement": 2006},
    {"nom": "Persona 2", "any_naixement": 1924},
    {"nom": "Persona 3", "any_naixement": 1912},
    {"nom": "Persona 4", "any_naixement": 2012},
]

# Imprimir capçalera de la taula
print("{:<12} {:<12} {:<12}".format("Nom", "Any naixement", "Anys actuals"))
print("-" * 36)

# Imprimir dades de cada persona
for persona in persones:
    edat_actual = any_actual - persona["any_naixement"]
    print("{:<12} {:<12} {:<12}".format(persona["nom"], persona["any_naixement"], edat_actual))
