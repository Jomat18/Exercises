import random

list_numbers=[]
size = 3
range_numbers = 10
sum_ = 0
mult_ = 1

for i in range(size):
	list_numbers.append(random.randrange(1,range_numbers))
	sum_+=list_numbers[i]
	mult_*=list_numbers[i]

print (list_numbers)	

print ('La suma es ',sum_)
print ('La multiplicacion es ', mult_)	
