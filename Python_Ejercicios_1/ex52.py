a = int(input("Introdueix el primer número: "))
b = int(input("Introdueix el segon número: "))
suma = 0

for i in range(a, b+1):
    suma += i

print("La suma dels números entre {} i {} es {}".format(a,b,suma))
