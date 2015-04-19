from __future__ import division

def pythagoras():

	alist = []

	for b in range(1,500):
		print b
		a = (500000 - 1000*b)/ (1000 - b)
		print a
		if (a.is_integer()):
			alist.append(a)
			print a

	return alist

print(pythagoras())			



