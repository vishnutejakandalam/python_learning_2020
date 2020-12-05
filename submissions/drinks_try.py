# ALGORITHM
# 1. read inputs
# 2. lists temp = [], price = []
# 3. 
# 
# 
# 
# 


n = int(input("no of cans! "))
m = int(input("minutes taken to reach home! "))
k = int(input("Ambient temperature !"))
l = int(input("Lower limit "))
r = int(input("higher limit"))

min_prices = []
for i in range(1,n+1):
	ti = int(input("temp of "+str(i)+"th can"))
	pi = int(input("price of "+str(i)+"th can"))
	
	for j in range(m):
		if ti > k+1:
			ti-=1
		if ti < k-1:
			ti+=1
		if k-1 <= ti <= k+1:
			ti = k
	if l <= ti <= r:
		min_prices.append(pi)

if len(min_prices) == 0:
	print(-1)
else:
	print(min(min_prices))
#  price.min()
# 
# 