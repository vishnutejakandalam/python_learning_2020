n = int(input("Enter a number!"))
str = str(n)
l = len(str)
print(l)
count = 0
for i in range(l):
	if int(str[i]) == 4:
		count+= 1
print(count)
		