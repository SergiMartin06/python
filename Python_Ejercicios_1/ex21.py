def menu(b):

        print("""

                Menu
                1. Dibuix 1
                2. Dibuix 2
                3. Sortir
        
        
        """)

        opcio=input("Seleccioan una opcio: ")
        return opcio



def crear_puntos(a):
        match a:
                case "1":
                        print("""            .
                                        .        .
                                .                .


                                .                 .
                                        .         .
                                        .   """)
                
                case "2":
                        print("""
                        
                        .       .       .
                        .       .       .
                        .       .       .
                        
                        """)


                case other:
                        print("Adeu")




