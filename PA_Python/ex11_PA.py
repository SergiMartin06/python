try:
	f = open("passwd'","r")
except IOError:
	print("Error d'entrada i sortida.")
except:
	print("Aquí arribarà si l'error és d'un altre tipus")
else:
	print("Aquí farem feina amb el fitxer")
finally:
	if not(f.closed): # Realment això donarà error si ha saltat una excepció
        f.close()

	with open('/etc/passwd', 'r') as f:
        for line in f:
            print(line)