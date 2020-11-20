n = input("enter a number: ")
l = len(n)
def max_two(a,b):
	if a>b:
		return a
	elif a<b:
		return b
	else:
		return a 
	
# count = {
# 	"count_0":0,
# 	"count_1":0
# }
count = [0] * 2 # [0,0]
for i in range(l):
	if n[i] == '0': 
		count[0]+= 1
	elif n[i] == '1':
		count[1]+=1
	else:
		exit()
max_n = max(count)
if max_n == l-1:
	print("Yes")
else:
	print("No")