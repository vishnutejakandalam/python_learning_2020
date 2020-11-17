number=int(input("enter a number: "))
# sqrt = number ** 0.5
# print("square root:", sqrt)

def sqrt_or_not(number): # Function defnition 
    sqrt = number ** 0.5
    sqrt = str(sqrt)
    if sqrt.split(".")[1] == "0":
        return True
    else:
        return False
    

print(
24," ",
sqrt_or_not(24),
16," ", 
sqrt_or_not(16),
number," ", 
sqrt_or_not(number),
36," ",
sqrt_or_not(36),
110," ",
sqrt_or_not(110),
114," ",
sqrt_or_not(114),
64," ",
sqrt_or_not(64),sep = ":")




