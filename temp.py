while(True):
    with open("test.txt", 'a') as f:
        name = input("ENter your name ")
        if name == "exit":
            break;
        f.write(name+"\n")
                
