import os
os.chdir("/home/professorat/AO")
os.getcwd() # Ens assegurem que estem en el directori que volem
os.mkdir("Prova")
os.getcwd() # Ens assegurem que estem en el directori que volem
a = ["Adrià", "Aroa", "Sebas", "Eric", "Sergi Pons", "Sergio Bolívar", "Sergi Martín", "Oscar", "Dani", "Ainhoa", "Aram", "Jade", "Isaac"]
with open("Ex12.txt","w") as f:
	for e in a:
		f.write(e+"\n")
with open("Ex12.txt","a") as f:
