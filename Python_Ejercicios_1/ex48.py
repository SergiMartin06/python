def crear_llista_fitxer(nom_fitxer):
    with open(nom_fitxer, 'r') as f:
        contingut = f.read()
    paraules = contingut.split()
    return paraules


l=crear_llista_fitxer(documento1.txt)
print(l)