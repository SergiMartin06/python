def long(frase):
    l=[]
    return list(map(len,frase.split(".")))

print(long("Hola, com estas?"))