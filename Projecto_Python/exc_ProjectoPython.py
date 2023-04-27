import random as random

def armarBaraja():
baraja = []
#EJEMPLO CARTA: ROJA 6, VERDE 4, AMARILLO SALTADO
colores = ["ROJO","VERDE","AZUL","AMARILLO"]
valores = [0,1,2,3,4,5,6,7,8,9,"+2", "SALTADO", "REVERSA"]
comodines = ["COMODIN","COMODIN +4"]
for color in colores:
    for valor in valores:
        cartaVal = "{} {}".format(color, valor)
        baraja.append(cartaVal)
        if valor != 0:
            baraja.append(cartaVal)
            for i in range(4):
                baraja.append(comodines[0])
                baraja.append(comodines[1])
        return baraja

def shuffleDeck(baraja):
    for cartaPos in range(len(baraja)):
        randPos=random.randint(0, 107);
        baraja[cartaPos], baraja[randPos] = baraja[randPos], baraja[cartaPos]
    return baraja


def sacarCarta(numCartas):
    cartasDib = []
    for x in range(numCartas):
        cartasDib.append(unoBaraja.pop(0))
    return cartasDib


def mostrarMano(jugador, mazo):
    print("JUGADOR {} TURNO".format(jugador+1))
    print("TU MAZO")
    print("-------------------")
    y = 1
    for carta in mazo:
        print("{}) {}".format(y, carta))
        y+=1
        print("")


def puedoJugar(color, valor, mazo):
    for carta in mazo:
        if "COMODIN" in carta:
            return True
        elif color in carta or valor in carta:
            return True
            return False

unoBaraja=armarBaraja();
unoBaraja=shuffleDeck(unoBaraja);
unoBaraja=shuffleDeck(unoBaraja);
desecho = []

jugadores = []
colores = ["ROJO","VERDE","AZUL","AMARILLO"]
numJugadores = int(input("DE CUANTOS JUGADORES? "))
while numJugadores<2 or numJugadores>4:
    numJugadores = int(input("NO VALIDO. PORFAVOR INGRESE UN NÚMERO ENTRE 2-4. DE CUANTOS JUGADORES? "))
for jugador in range(numJugadores):
    jugadores.append(sacarCarta(5))

turnoJugador = 0
direccionJuego = 1
jugando = True
desecho.append(unoBaraja.pop(0))
separarCarta = desecho[0].split(" ", 1)
colorActual = separarCarta[0]
if colorActual != "COMODIN":
    cartaVal = separarCarta[1]
else:
    cartaVal = "ANY1"

while jugando:
    mostrarMano(turnoJugador, jugadores[turnoJugador])
    print("CARTAS EN LA PARTE SUPERIOR DE LA PILA DE DESECHOS: {}".format(desecho[-1]))
    if puedoJugar(colorActual, cartaVal, jugadores[turnoJugador]):
        cartaElegida = int(input("CON CUAL CARTA QUIERES JUGAR? "))
while not puedoJugar(colorActual, cartaVal,[jugadores[turnoJugador][cartaElegida-1]]):
    cartaElegida = int(input("CARTA NO VALIDA.CON CUAL CARTA QUIERES JUGAR? "))
    print("JUGASTE {}".format(jugadores[turnoJugador][cartaElegida-1]))
    desecho.append(jugadores[turnoJugador].pop(cartaElegida-1))

if len(jugadores[turnoJugador])==0:
    jugando = False
    ganador = "JUGADOR {}".format(turnoJugador+1)
else:
    separarCarta = desecho[-1].split(" ", 1)
    colorActual = separarCarta[0]

if len(separarCarta) == 1:
    cartaVal = "ANY"
else:
    cartaVal = separarCarta[1]
if colorActual == "COMODIN":
    for x in range(len(colores)):
        print("{}) {}".format(x+1, colores[x]))
    nuevoColor = "A QUE COLOR LO QUIERES CAMBIAR? "
while nuevoColor < 1 or nuevoColor > 4:
    nuevoColor = int(input("OPCION NO VALIDA. A QUE COLOR LO QUIERES CAMBIAR? "))
    colorActual = colores[nuevoColor-1]
if cartaVal == "REVERSA":
    direccionJuego = direccionJuego * -1
elif cartaVal == "SALTADO":
    turnoJugador += direccionJuego
if turnoJugador >= numJugadores:
    turnoJugador = 0
elif turnoJugador < 0:
    turnoJugador = numJugadores-1
elif cartaVal == "+2":
    jugadora = turnoJugador+direccionJuego
if jugadora == numJugadores:
    jugadora = 0
elif jugadora < 0:
    jugadora = numJugadores-1
    jugadores[jugadora].extend(sacarCarta(2))
elif cartaVal == "COMODIN +4":
    jugadora = turnoJugador+direccionJuego
if jugadora == numJugadores:
    jugadora = 0
elif jugadora < 0:
    jugadora = numJugadores-1
    jugadores[jugadora].extend(sacarCarta(4))
    print("")
else:
    print("NO PUEDES JUGAR. TIENES QUE TOMAR UNA CARTA.")
    jugadores[turnoJugador].extend(sacarCarta(1))

turnoJugador += direccionJuego
if turnoJugador >= numJugadores:
    turnoJugador = 0
elif turnoJugador < 0:
    turnoJugador = numJugadores-1

print("PERDISTE ERES UN LOSER")
print("{} ES EL GANADOR!!".format(ganador))