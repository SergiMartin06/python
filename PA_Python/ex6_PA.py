def numi(l):
		return len([e for i,e in enumerate(l) if e==i])
print(numi([0,2,2,1,5,5,6,10]))
