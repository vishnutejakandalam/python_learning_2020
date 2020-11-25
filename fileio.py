#read, write, append

with open("file.txt",'a') as f: 
# f = open("file.txt", 'r')
    # for line in f:
    #     print(line)
    f.write("\n THIS IS WROTE BY PYTHON CODE")
print("File closed")




