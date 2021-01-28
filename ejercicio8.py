from heapq import heappush, heappop
import random

size = 10
array = []
array_capicua = []

for i in range(size):
	array.append(random.randint(100, 999))

print (array)	

def ordenar(array):
	h = []
	size = len(array)
	for element in array:
	    heappush(h, element)
	
	return [heappop(h) for i in range(size)]


def capicua(array):

	for number in array:
		right = number%10
		left = int(number/100)

		if right==left:
			array_capicua.append(number)

	print (ordenar(array))		

capicua(array)

