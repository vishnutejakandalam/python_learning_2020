p = int(input("enter amount:  "))  #p = 10
power = 2048
count = 0
string = ""
sums = 0

while True:
	if p<power:
		string+="0 "
		power/=2
		print()
		print("string ",string)
	elif p>power:
		string+=
		p= p - power
		sums+=power
		print(power, p)
		print("string ",string)
		count+=1
	elif p==power:
		string+="1"
		sums+=power
		count+=1
		break;

if len(string) != 12:
	string+="0"*(12-len(string))
print(count,len(string), string,sums, sep="   ")










# for i in range(12):
# 	print(p_sum, 2**i, sep = ", ")
# 	p_sum = p_sum + 2**i
# 	count+=1
# 	if p == p_sum:
# 		break 
	

# while(p_sum > p):
# 	print(p_sum)
# 	p_sum-=2**i
# 	i-=1
# 	count+=1
# print(count)



# for i in range(12):
# 	sum = 2**i
# 	if p != sum:
# 		sum = sum + 2**i
# 		continue
# 		count+=2**i
# print(min(count))