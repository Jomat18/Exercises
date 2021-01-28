
def serie(list_):	 
	stack = []

	for elem in list_:
		if elem!=')':
			stack.append(elem)
		else:
			try:
				stack.pop()
			except IndexError:	
				return False			

	return not bool(len(stack))		


print (serie('(()()())()()(())'))
print (serie('(()('))
#print (serie(')()(()'))

