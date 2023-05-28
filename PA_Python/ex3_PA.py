def paraula_llista(lista,letra):
    return list(filter(lambda a: a[:1]==letra,lista))

print(paraula_llista(['azada','balcon'],'b'))