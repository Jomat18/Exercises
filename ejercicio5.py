import random

list_numbers=[]
size = 3
range_numbers = 10

for i in range(size):
	list_numbers.append(random.randrange(1,range_numbers))


def sum(list):
	sum_ = 0

	for element in list:
		sum_+=element

	return sum_

def mult(list):
	mult_ = 1	

	for element in list:
		mult_*=element

	return mult_

print (list_numbers)	

print ('La suma es ',sum(list_numbers))
print ('La multiplicacion es ', mult(list_numbers))	
