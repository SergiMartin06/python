def llegir_numero():
    return(int(input("Introdueix un valor: ")))

def llegir_interes_float():
    return(float(input("Introdueix un valor real: ")))

def calcular_prestec(q,i,a):
    return (q*(1+i/100)**a)

q=llegir_numero()
i=llegir_interes_float()
a=llegir_numero()
c=calcular_prestec(q,i,a)
print("Si solicito {} a un interes anual del {} a {} anys, al final pagare {} euros".format(q,i,a,c))