def multiple(x):
	prime_nos = [2,3,5,7,11,13,17,19]
	prod = 1
	for p in prime_nos:
		prod *= p
		n = 2
		while (p**n < 21):
			prod *= p
			n +=1
	return prod
	

print(multiple(20))			



#num - factorize and list
#then factorize and add factors which are not already,present