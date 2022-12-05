def es_palindromo(a):
    inicio = 0
    fin = len(a) - 1
    while a[inicio] == a[fin]:
        if inicio >= fin:
            return True
        inicio += 1
        fin -= 1
    return False

a = input ("Añade una palabra: ")
if (True):    
    print("Si es")
else:
    print("No es")
