t=int(input("no of test cases"))
	
for i in range(t):
	a=int(input())	
	b=int(input())
	c=int(input())
	d=int(input())
	rectangle = set([a,b,c,d])
	if len(rectangle) == 2:
		print("YES")
	else:
		print("NO")


	# count=0
	# if a==b or a==c or a==d:
	# 	count+=1
	# if b==c or b== d or b== a:
	# 	count+=1
	# if c==d or c==a or c==b:
	# 	count+=1
	# if d==a or d==b or d==c:
	# 	count+=1
	# 	print(count)	
			
	# if count == 4:
	# 	print("YES")
	# else:
	# 	print("NO")
	

