a =[15,20,55,56,65,72,81,96,10.65] 
b = [1,2,3,4,5]


# scope and lifetime of variables 

def sum_of_list(a:list):         # funcion defnition
    sumall = 0 # variable defnition
    for i in a:
        sumall = sumall + i
    return sumall




function_value = sum_of_list(a)
f = sum_of_list(b)
print(function_value)
print(f)


# we call lists as arrays in C


