def calculadora():
    print("""
    
    1.Suma
    2.Resta
    
    
    """)

op=int(input(""))
match op:
    case 1:
        a=int(input("Selecciona 1 valor: "))
        b=int(input("Selecciona 2 valor: "))
        