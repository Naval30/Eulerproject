def multipl():
	listj = []
	b = 0
	for y in range(1000):
		if y%5 == 0 and y%3 == 0:
			b += y
		elif y%5 == 0 or y%3 == 0:
			b += y
	return b		 
		 	

	
				

print multipl()