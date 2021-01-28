
import random

def generate_array(size, range_numbers):
	array = []

	for i in range(size):
		array.append(random.randrange(range_numbers))

	return array

def distinct(array):

	table_hash = {}

	print (array)

	for element in array:
	
		if element in table_hash:
			table_hash[element] += 1
		else:
			table_hash[element]= 1

	for element in table_hash:
		if table_hash[element]==1:
			print (element)



size = 20
range_numbers = 10

array = generate_array(size, range_numbers)
distinct(array)


'''
Teoria de SQL:
- Defina indice en base datos:

Es una estructura de datos que mejora la velocidad de operaciones, minimizando el numero de accesos a disco

- como hacer un flujo de respaldo, 

mysqldump -u root -p database_name > D:\Backup\database_name.sql

- como operar con null

con NULLIF(), Case, COALESCE(), ISNULL(),  IS NULL y IS NOT NULL

'''

