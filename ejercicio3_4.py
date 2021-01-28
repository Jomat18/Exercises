'''
Pregunta 3:
 
Que es INDEX (indice) en base de datos, indicar beneficios y desventajas

Es una estructura de datos que mejora la velocidad de operaciones, minimizando el numero de accesos a disco

Desventaja
- Consumir toda la memoria con indices podria ser un problema, ya que los indices ocupen espacio en disco y en memoria.
- Cuando se insertar, elimina y actualizan datos se ralentiza las consultas, porque se tienen que actualizar los indices

Ventajas 
- Cuando solo se necesita un subconjunto de filas en un tabla evita leer la tabla completa.
- Evitan que datos repetidos entre a una tabla

'''
import os 
import filecmp 

path = os.getcwd()
directory = os.listdir(path)

content = []

def folder_files():

	for file_folder in directory: 
		content.append(file_folder)

	print (' ------- Contenido \n')
	print (content)
	
	# ordenando por tamaño
	print ('\n ------- Ordenado por tamaño')
	content.sort(key=os.path.getsize)
	print (content)

	# ordenando por fecha
	print ('\n ------- Ordenado por fecha')
	content.sort(key=os.path.getctime)	

	print (content,'\n')

	size = len(content)

	for i in range(size):
		for j in range(i+1,size):
			comp = filecmp.cmp(content[i], content[j], shallow = False) 
			if comp:
				print ('Duplicados en contenido ', content[i], content[j])

folder_files()		