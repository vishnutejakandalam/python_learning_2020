#sample run

n = int(input("no of cans! "))   #2
m = int(input("minutes taken to reach home! "))  #3
k = int(input("Ambient temperature !")) # 22
l = int(input("Lower limit "))			# 10
r = int(input("higher limit"))			# 15

temperatures = []
min_prices = []
print("t")
for i in range(n):
	data = int(input())
	temperatures.append(data) 	# 8, 19
	
prices=[]
print("p")
for f in range(n):
	data = int(input())
	prices.append(data) 	# 3, 3.5

for i in range(n): 		#0, 1
	for j in range(m): # 0, 1, 2
		if temperatures[i]> k+1:
			temperatures[i]-=1
		if temperatures[i]< k-1:	#8<21, 9<21, 10<21; 19<21, 20<21
			temperatures[i]+=1	#9, 10, 11; 20, 21
		if k-1 <= temperatures[i] <= k+1: #21<=21<=23
			temperatures[i]=k #22
	if l <= temperatures[i] <= r:
		#min_prices.append(prices[0])
		print("Appending ",i,"th can price to min prices")
		min_prices.append(prices[i])
	
if len(min_prices) == 0:
	print(-1)
else:
	print(temperatures,prices)
	print(min(min_prices))