#Exceptions
# try:
    # try if the following code generates errors or not
    # print("hello world")
# except:
    #catch if any error occurs in the try block and executes this...
    # print("It will save...")
# else:
    #if there was no problem with try block then this will be executed...
    # print("else")

def take_input():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    return a,b
def devide(a,b):
    return a/b
# if b == 0:
#     print("Cannot devide by zero dude! ")
#     exit()
    x,y = take_input()
# try:
#     print(devide(x,y))
# except:
#     print("B must not be zero.")
#     x,y = take_input()
#     print(devide(x,y))

try:
    std_id = 0
    std_id = int(input("enter your student id"))
except:
    print("Error in input\n")
else:
    with open("std_details.txt", 'a') as file:
        file.write(str(std_id)+"\n")
print("THIS IS PRINTING BECAUSE OF PYTHON....")
