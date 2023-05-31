class Vehicle:
    numvehicles = 0 # Var de la classe
    def __init__(self, nom):
        self.nom = nom # Var de l’objecte i pública
        self.velocitat = 0
        self._protected_var = 10 # Var de l’objecte i protected (1 underscore)
        self.__private_var = 20   # Var de l’objecte i privada (2 underscore)
    
    def acceleració(self):
        self.velocitat+=1
    
    def renou_motor(self):
       pass


objecte = Vehicle # Cream un objecte Vehicle
print(objecte._protected_var) # Podem, encara que no és recomanable, accedir directament a la variable protegida de l’objecte.
print(objecte.__private_var) # Això donarà error, no ho podem fer.