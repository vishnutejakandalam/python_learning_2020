"""Program to print all the factors of a composite number ...."""

# taking a number from keyboard and converting to int
n = int(input("Enter a number:"))
def is_composite(number):
    count = 0
    comp_factors = []
    for i in range(1,number+1):
        if number % i ==0:
            count+=1
            comp_factors.append(i)
    print()
    if count > 2:
        print("the number is composite number")
        return comp_factors
    else:
        printf("The number is prime.")

# function call
l = is_composite(n)
print(l)
print()



        
