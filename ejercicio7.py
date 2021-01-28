
def n_fibonaci(n):

	fibonaci = [0, 1]

	for i in range(2,n+1):
		fib = fibonaci[i-1] + fibonaci[i-2]
		fibonaci.append(fib)

	return fibonaci[n]	

print (n_fibonaci(14))	

