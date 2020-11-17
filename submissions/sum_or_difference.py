n1 = int(input("enter n1: "))
n2 = int(input("enter n2: "))
if n1 in range(10,100) and n2 in range(10,100):
	if n1> n2:
		print(n1-n2)
	else:
		print(n1+n2)
else:
	exit(0)


