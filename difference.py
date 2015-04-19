def diff(n):
	sum1 = ((n*(n+1))/2)**2
	#sum1 = sum1 * sum1
	sum2 = (n*(n+1)*(2*n+1))/6
	diff =  sum1 - sum2
	print sum1
	print sum2
	print diff


print(diff(100))		

