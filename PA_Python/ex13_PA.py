class Animal:
    def __init__(self, especie, edat):
        self.edat=edat
        self.especie=especie
    def xerrar(self):
        pass
    def moure(self):
        pass
    def quisoc(self):
        print("Soc un {}".format(self.especie))

class cavall(Animal):
    def xerrar(self):
        print("hiiiii")
    def moure(self):
        print("galopa, fa trot i pas")

class delfin(Animal):
    def xerrar(self):
        print("chasss")
    def moure(self):
        print("")

class abeja(Animal):
    def xerrar(self):
        print("bzzzzzz")
    def moure(self):
        print("Vuela")
    def picar(self):
        print("te pica el culo")

class humano(Animal):
    def __init__(self, especie, edat, nom):
        super().__init__(especie,edat)
        self.nom=nom
    def xerrar(self):
        print("blababablaablaba")
    def moure(self):
        print("Caminabpvaino`rdnfàbpoain")
    def quisoc(self):
        print("Soc un huma i me dic {}".format(self.nom))

class hijo(humano):
    def xerrar(self):
        print("blablablabla")
    def moure(self):
        print("camina a dos patas")
    def __init__(self, especie, edat, nom, pares):
        super().__init__(especie, edat, nom)
        self.pares=pares
    def nompares(self):
        print("El meu pare es diu {} i la meva mare {}".format(self.pares[0], self.pares[1]))

class centaure(cavall,humano):
    def quisoc(self):
        print("Soc un centaure i sorgeix de {} ".format(centaure.__mro__))

class xou:
    def quisoc(self):
        print("Duck type, això és el que sóc")
    def moure(self):
        print("Duck type, així em moc")
    def xerrar(self):
        print("Duck type, així xerr")
        

f = [humano("Humà","32","Joan"), cavall('mamífer', 10), delfin('mamífer', 23), abeja('insecte', 1), hijo("Humà","6","Pau",("Joan","Luz")), xou(), centaure("Centaure","40","Quiron")]

for e in f:
	e.quisoc()
	e.moure()
	e.xerrar()
if type(e)==hijo:
    e.nompares()
if type(e)==abeja:
    e.picar()