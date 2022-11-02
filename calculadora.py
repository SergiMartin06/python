print("""
Menu:
1. Sumar
2. Restar
3. Multiplicar
4. Dividir
0. Sortir
""")

opcio=input ("Selecciona l'opcio que vulgui: ")
a= input("Indiqui el primer operand: ")
b= input("Indiqui el segon operand: ")

match opcio:
    case '1':
        c=int(a)+int(b) 
        print("La suma de ",a," mes ",b," es ", c)
    case '2':
        c=int(a)-int(b)
        print("La resta de ",a," menys ",b," es ", c)
    case '3': 
        c=int(a)*int(b)
        print("La multiplicacio de ",a," per ",b," es ", c)
    case '4': 
        c=int(a)/int(b)
        print("La divisio de ",a," entre ",b," es ", c)
    case '0': 
        print("Adeu")
    case other:
        print("opcion no valida")


