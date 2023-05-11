import random

def llista_20_elements(a):
    return random.sample(range(1, 101), 20)


def hi_ha_duplicats(lst):
    if len(set(lst)) != len(lst):
        print("Si hay repes")
    else:
        print("No hay repes")


l=[]
print(llista_20_elements(l))
hi_ha_duplicats(l)