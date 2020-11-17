"""Python program to add two numbers using funcions"""

def add(a,b): # funcion defnition , Called funcion
    # a,b formal parameters
    print("from Called funcion, ",a+b)
    c = a+b
    return c

def sub(a,b):
    c = a-b

def mul(a,b):
    c = a*b
    print("Multiplying numbers een though it isn't called ")
    return c

x = 10
y = 20
print("Calling a funcion ")
print("From calling funcion, ",add(x,y)) #function call, Calling funcion
# x,y actual parameters
print("Returned from a funcion")
print("The substraction is, ",sub(x,y)) 
