import random as rnd
import math

# INGRESO
n = int(input('numero de dardos: '))

# PROCEDIMENTO
premio = 0
i = 0
while (i<n):
    x = (rnd.random()*160)-80
    y = (rnd.random()*160)-80
    d = math.sqrt(x**2+y**2)

    if (d<10):
        premio = premio + 50
    if (d>=10 and d<40):
        premio = premio + 40
    if (d>=40 and d<80):
        premio = premio + 30

    i = i+1

# SALIDA
print(' El total ganado es:')
print(premio)