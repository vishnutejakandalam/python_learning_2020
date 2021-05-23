b=int(input("budget"))
n=int(input("tablets"))

favourable_areas = []
w=[]
print("w")
for i in range(n):
	w.append(int(input()))
	
h=[]
print("h")
for f in range(n):
	h.append(int(input()))
	

p=[]
print("p")
for s in range(n):
	data= int(input())
	p.append(data)
	
for i in range(n):
	if p[i]<=b:
		favourable_areas.append(h[i]*w[i])
		
if len(favourable_areas)>=1:
	print(max(favourable_areas))
else:
	print("No Tablet")
	
