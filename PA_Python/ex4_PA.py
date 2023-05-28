def concateni(l, p, con):
	return [a+con+b for (a,b) in zip(l,p)]
print(concateni(['acana'],['dor'],'-'))
