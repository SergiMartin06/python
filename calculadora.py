def menu_principal():
    print("""
    Calculadora
    Menu:
    1. Numeros enteros
    2. Numeros reales
    3. Canvis de base
    0. Sortir
    """)

    opcio=input("Selecciona l'opcio que vulgui: ")
    return opcio 

def menu_enters():
    print("""
            Menu Calculadora de nuemros enteros
            1. Sumar
            2. Restar
            3. Multiplicar
            4. Dividir
            5. Potencia
            6. Modul
            7. Cociente
            0. Sortir
            """)

    opcio=input("Selecciona l'opcio que vulgui: ")
    return opcio 

def menu_reals():
    print("""
            Menu Calculadora de nuemros enteros
            1. Sumar
            2. Restar
            3. Multiplicar
            4. Dividir
            5. Potencia
            0. Sortir
            """)

    opcio=input("Selecciona l'opcio que vulgui: ")
    return opcio 

def menu_canvis_de_base():
    print("""
            Menu Calculadora de cambios de base
            1. Pasar de decimal a binario, octal y hexadecimal
            2. Pasar de Binario a decimal, octal y hexadecimal
            3. Pasar de Octal a binario, decimal y hexadecimal
            4. Pasar de Hexadecimal a Binario, Octal y Decimal
            0. Sortir
            """)


#Funcions menu 3 cambios de base

#Decimal a ...

def dectobin(numero_decimal):
    numero_binario = 0
    multiplicador = 1

    while numero_decimal != 0:
        # se almacena el módulo en el orden correcto
        numero_binario = numero_binario + numero_decimal % 2 * multiplicador
        numero_decimal //= 2
        multiplicador *= 10

    return numero_binario


def dectooctal(decimal):
    octal = ""
    while decimal > 0:
        residuo = decimal % 8
        octal = str(residuo) + octal
        decimal = int(decimal / 8)
    return octal

#Base 16

def obtener_caracter_hexadecimal(valor):
    # Lo necesitamos como cadena
    valor = str(valor)
    equivalencias = {
        "10": "a",
        "11": "b",
        "12": "c",
        "13": "d",
        "14": "e",
        "15": "f",
    }
    if valor in equivalencias:
        return equivalencias[valor]
    else:
        return valor

def dectohexadecimal(decimal):
    hexadecimal = ""
    while decimal > 0:
        residuo = decimal % 16
        verdadero_caracter = obtener_caracter_hexadecimal(residuo)
        hexadecimal = verdadero_caracter + hexadecimal
        decimal = int(decimal / 16)
    return hexadecimal


#Binario a decimal

def bintodecimal(numero_binario):
	numero_decimal = 0 

	for posicion, digito_string in enumerate(numero_binario[::-1]):
		numero_decimal += int(digito_string) * 2 ** posicion

	return numero_decimal

#Binario a octal

print("Enter the Binary Number: ")
binarynum = int(input())

octaldigit = 0
octalnum = []
i = 0
mul = 1
chk = 1
while binarynum!=0:
    rem = binarynum % 10
    octaldigit = octaldigit + (rem * mul)
    if chk%3==0:
        octalnum.insert(i, octaldigit)
        mul = 1
        octaldigit = 0
        chk = 1
        i = i+1
    else:
        mul = mul*2
        chk = chk+1
    binarynum = int(binarynum / 10)

if chk!=1:
    octalnum.insert(i, octaldigit)

print("\nEquivalent Octal Value = ", end="")
while i>=0:
    print(str(octalnum[i]), end="")
    i = i-1
print()


#Binario a hexadecimal


def binToHexa(n):
    bnum = int(n)
    temp = 0
    mul = 1
      
    # counter to check group of 4
    count = 1
      
    # char array to store hexadecimal number
    hexaDeciNum = ['0'] * 100
      
    # counter for hexadecimal number array
    i = 0
    while bnum != 0:
        rem = bnum % 10
        temp = temp + (rem*mul)
          
        # check if group of 4 completed
        if count % 4 == 0:
            
            # check if temp < 10
            if temp < 10:
                hexaDeciNum[i] = chr(temp+48)
            else:
                hexaDeciNum[i] = chr(temp+55)
            mul = 1
            temp = 0
            count = 1
            i = i+1
              
        # group of 4 is not completed
        else:
            mul = mul*2
            count = count+1
        bnum = int(bnum/10)
          
    # check if at end the group of 4 is not
    # completed
    if count != 1:
        hexaDeciNum[i] = chr(temp+48)
          
    # check at end the group of 4 is completed
    if count == 1:
        i = i-1
          
    # printing hexadecimal number
    # array in reverse order
    print("\n Hexadecimal equivalent of {}:  ".format(n), end="")
    while i >= 0:
        print(end=hexaDeciNum[i])
        i = i-1
  
# Driver code
if __name__ == '__main__':
    binToHexa('1111')
    binToHexa('110101')
    binToHexa('100001111')
    binToHexa('111101111011')



#Octala a ...

def octal_a_decimal(octal):
    decimal = 0
    posicion = 0
    # Invertir octal, porque debemos recorrerlo de derecha a izquierda
    # pero for in empieza de izquierda a derecha
    octal = octal[::-1]
    for digito in octal:
        valor_entero = int(digito)
        numero_elevado = int(8 ** posicion)
        equivalencia = int(numero_elevado * valor_entero)
        decimal += equivalencia
        posicion += 1
    return decimal


#Octal a binario

print("Enter the Octal Number: ")
octnum = int(input())

rev = 0
chk = 0

while octnum!=0:
    rem = octnum%10
    if rem>7:
        chk = 1
        break
    rev = rem + (rev*10)
    octnum = int(octnum/10)

if chk == 0:
    octnum = rev
    binnum = ""

    while octnum!=0:
        rem = octnum%10
        if rem==0:
            binnum = binnum + "000"
        elif rem==1:
            binnum = binnum + "001"
        elif rem==2:
            binnum = binnum + "010"
        elif rem==3:
            binnum = binnum + "011"
        elif rem==4:
            binnum = binnum + "100"
        elif rem==5:
            binnum = binnum + "101"
        elif rem==6:
            binnum = binnum + "110"
        elif rem==7:
            binnum = binnum + "111"
        octnum = int(octnum/10)

    print("\nEquivalent Binary Value = ", binnum)

else:
    print("\nInvalid Input!")


#Octal a hexadecimal

print("Enter the Octal Number: ")
octnum = int(input())

chk = 0
i = 0
decnum = 0
while octnum!=0:
    rem = octnum%10
    if rem>7:
        chk = 1
        break
    decnum = decnum + (rem * (8 ** i))
    i = i+1
    octnum = int(octnum/10)

if chk == 0:
    i = 0
    hexdecnum = []
    while decnum != 0:
        rem = decnum % 16
        if rem < 10:
            rem = rem + 48
        else:
            rem = rem + 55
        rem = chr(rem)
        hexdecnum.insert(i, rem)
        i = i + 1
        decnum = int(decnum / 16)

    print("\nEquivalent Hexadecimal Value is: ")
    i = i - 1
    while i >= 0:
        print(end=hexdecnum[i])
        i = i - 1
    print()

else:
    print("\nInvalid Input!")



#Hexadecimal a ...

def obtener_valor_real(caracter_hexadecimal):
    equivalencias = {
        "f": 15,
        "e": 14,
        "d": 13,
        "c": 12,
        "b": 11,
        "a": 10,
    }
    if caracter_hexadecimal in equivalencias:
        return equivalencias[caracter_hexadecimal]
    else:
        return int(caracter_hexadecimal)

#Hexadecimal a decimal

def hexadecimal_a_decimal(hexadecimal):
    # Convertir a minúsculas para hacer las cosas más simples
    hexadecimal = hexadecimal.lower()
    # La debemos recorrer del final al principio, así que la invertimos
    hexadecimal = hexadecimal[::-1]
    decimal = 0
    posicion = 0
    for digito in hexadecimal:
        print(f"Decimal es {decimal}")
        # Necesitamos que nos dé un 10 para la A, un 9 para el 9, un 11 para la B, etcétera
        valor = obtener_valor_real(digito)
        print(f"El verdadero valor de {digito} es {valor}")
        elevado = 16 ** posicion
        print(
            f"Elevamos 16 a la potencia {posicion}, el resultado es {elevado}")
        equivalencia = elevado * valor
        print(
            f"Multiplicamos el número elevado por el valor del carácter actual: {equivalencia}")
        decimal += equivalencia
        print(f"Ahora decimal es {decimal}")
        posicion += 1
    return decimal


#Hexadecimal a binario

import math 
  
ini_string = "1a"
  
print ("Initial string", ini_string) 
  
res = "{0:08b}".format(int(ini_string, 16)) 
  
print ("Resultant string", str(res)) 


#Hexadecimal a Octal

print("Enter the Hexadecimal Number: ")
hexdecnum = input()

chk = 0
decnum = 0
hexdecnumlen = len(hexdecnum)
hexdecnumlen = hexdecnumlen-1
i = 0
while hexdecnumlen>=0:
    rem = hexdecnum[hexdecnumlen]
    if rem>='0' and rem<='9':
        rem = int(rem)
    elif rem>='A' and rem<='F':
        rem = ord(rem)
        rem = rem-55
    elif rem>='a' and rem<='f':
        rem = ord(rem)
        rem = rem-87
    else:
        chk = 1
        break
    decnum = decnum + (rem * (16 ** i))
    hexdecnumlen = hexdecnumlen-1
    i = i+1

if chk==0:
    i = 0
    octnum = []
    while decnum!=0:
        rem = decnum%8
        octnum.insert(i, rem)
        i = i+1
        decnum = int(decnum/8)

    print("\nEquivalent Octal Value is: ")
    i = i-1
    while i>=0:
        print(octnum[i], end="")
        i = i-1
    print()
else:
    print("\nInvalid Input!")


# Progrma principal de la calculadora
opcio=1
while(opcio!=0):
    opcio= menu_principal()
    match opcio:
        case "1":
            opcio2=menu_enters()
            a = int(input("Indiqui el primer operand: "))
            b = int(input("Indiqui el segon operand: "))

            match opcio:
                case "1":
                    c=int(a)+int(b) 
                    print("La suma de ",a," mes ",b," es ",c)
                case "2":
                    c=int(a)-int(b)
                    print("La resta de ",a," menys ",b," es ",c)
                case "3": 
                    c=int(a)*int(b)
                    print("La multiplicacio de ",a," per ",b," es ",c)
                case "4": 
                    c=int(a)/int(b)
                    print("La divisio de ",a," entre ",b," es ",c)
                case "5":
                    c= (a) ** (b)
                    print("La potencia de ",a," elevat a ",b," es ",c)
                case "6":
                    c= (a) % (b)
                    print("El modul de ",a," mòdul ",b," és ",c)
                case "7":
                    c= (a) // (b)
                    print("El cociente de ",a," entre ",b," es ",c)
                case "0": 
                    print("Adeu")
                case other:
                    print("opcion no valida")

        case "2":
            opcio=menu_reals()
            a = float(input("Indiqui el primer operand: "))
            b = float(input("Indiqui el segon operand: "))
                    
            match opcio:
                case "1":
                    c=int(a)+int(b) 
                    print("La suma de ",a," mes ",b," es ", c)
                case "2":
                    c=int(a)-int(b)
                    print("La resta de ",a," menys ",b," es ", c)
                case "3": 
                    c=int(a)*int(b)
                    print("La multiplicacio de ",a," per ",b," es ", c)
                case "4": 
                    c=int(a)/int(b)
                    print("La divisio de ",a," entre ",b," es ", c)
                case "5":
                    c= (a) ** (b)
                    print("La potencia de ",a," elevado a ",b," es ",c)
                case "0": 
                    print("Adeu")
                case other:
                    print("opcion no valida")

        case "3":
            opcio=menu_canvis_de_base()

            opcio =input("Indica la opcio que vulguis")
            a =input("Indiqui el nuombre: ")
                
            match opcio2:
                case "1": # Binari a
                    b=int(a,base=8)
                    c=int(a,base=10)
                    d=int(a,base=16)
                    print("El número ",a," en octal= ",b, " en decimal= ",c," en hexadecimal= ", d)
                case "2": # Octal a
                    b=int(a,base=2)
                    c=int(a,base=10)
                    d=int(a,base=16)
                    print("El número ",a," en binari= ",b, " en decimal= ",c," en hexadecimal= ", d)
                case "3": # Decimal a
                    b=int(a,base=2)
                    c=int(a,base=8)
                    d=int(a,base=16)
                    print("El número ",a," en binari= ",b, " en octal= ",c," en hexadecimal= ", d)
                case "4": # Hexadecimal a
                    b=int(a,base=2)
                    c=int(a,base=8)
                    d=int(a,base=10)
                    print("El número ",a," en binari= ",b, " en octal= ",c," en decimal= ", d)
                case "0":
                    print("Adéu")
                case other:
                    print("Opció no vàlida!")
        case "0":
            print("Adéu")