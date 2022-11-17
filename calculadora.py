opcio=1
while(opcio!=0):
    print("""
    Calculadora
    Menu:
    1. Numeros enteros
    2. Numeros reales
    3. Canvis de base
    0. Sortir
    """
    )
    
    opcio=input("Selecciona l'opcio que vulgui: ")
    match opcio:
        case "1":
            print("""
            Menu Calculadora de nuemros enteros
            1. Sumar
            2. Restar
            3. Multiplicar
            4. Dividir
            0. Sortir
            """)

            a = int(input("Indiqui el primer operand: "))
            b = int(input("Indiqui el segon operand: "))

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
                case "0": 
                    print("Adeu")
                case other:
                    print("opcion no valida")

        case "2":
                    print("""
                    Menu Calculadora de nuemros enteros
                    1. Sumar
                    2. Restar
                    3. Multiplicar
                    4. Dividir
                    0. Sortir
                    """)

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
                        case "0": 
                            print("Adeu")
                        case other:
                            print("opcion no valida")
        case "3":
                    print("""
                    Menu Calculadora de nuemros enteros
                    1. 
                    2. 
                    3. 
                    4. 
                    0. Sortir
                    """)

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
                        case "0": 
                            print("Adeu")
                        case other:
                            print("opcion no valida")


