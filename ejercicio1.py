from heapq import heapify, heappush, heappop
import random

heap = []
heapify(heap)

size = 10
sum_minor = 0
range_numbers = 100

for i in range(size):
	heappush(heap,random.randrange(range_numbers))

#print (heap)	

for i in range(int(size/2)):
	minor = heappop(heap)
	sum_minor+=minor

#print (heap)
sum_major = sum(heap)

print ('Suma menores: ', sum_minor)
print ('Suma mayores: ', sum_major)