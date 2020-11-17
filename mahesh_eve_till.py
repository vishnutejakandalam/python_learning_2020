#Scanning a value from keyboard
n=int(input('Enter a number:'))
#function defnition
def even_func(n):
	for i in range(n):
		if i % 2 == 0:
			print(i, end = " ")
	print()


#fuctin call
even_func(n)

