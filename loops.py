# for i in range(20,100,5):
#     print(i,end = "\t")
# print()


# initialisation
# condition check
# incrementation
# Prime numbers
n = int(input("Enter a number: "))
def is_prime(number):
    count = 0
    for i in range(1,n//2):
        if number%i == 0:
            count += 1
    if count == 2:
        print(number," is a Prime Number")
    else:
        print(number," is a Composite Number")
# is_prime(n)


i = -1

while(i<n):
    #body of the loop
    i+=1
    if i % 2 == 0:
        print(i,end = "\t")
    if i > 150:
        # continue
        break
    # print(i,end="\t")
print()



# break and continue
