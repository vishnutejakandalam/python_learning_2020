p = int(input("t"))   #p = 10
count = 0
for i in range(12):
	sum = 2**i
	if p != sum:
		sum = sum + 2**i
		continue
		count+=2**i
print(min(count))