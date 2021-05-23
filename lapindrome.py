n=input("enter a lapindrome !!")
if len(n)>6:
    exit()
#else:
    #print("dude")   
if len(n)==3:
    if n[0]==n[-1]:
        print("YES")
    else:
        print("No")    

if len(n)==4 or 5:
    if (n[0]==n[-1] or n[0] == n[-2]) and (n[1]==n[-1] or n[1]==n[-2]):
         print("YES")
    else:
        print("No")    

if len(n)==6:
    if  n[0]==n[-1] or n[-2]or n[-3] and n[1]==n[-1]or n[-2]or n[-3] and n[2]==n[-1]or n[-2]or n[-3]:
         print("YES")
    else:
        print("No")    




