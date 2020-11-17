"""program for withdrawal of amount in an atm center"""

a = int(input("ENter bank balance: "))
b = int(input("Enter amount you want to withdrawl: "))

def sub(a,b):
	if a>b and b% 5 == 0:
		c = a-b-0.5
		print("The available balance is: ",c)
	else:
		print("Unauthorised transaction:")

sub(a,b)
print()		

	