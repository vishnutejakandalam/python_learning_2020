

class data_exceptoin(Exception):
    def __init__(self, message):
        self.string=message
        print(self.string)
    def write(self):
        print(self.string)



std_class = int(input("enter the class you are studying. "))
if std_class > 12:
    raise(data_exceptoin("invalid class"))
section = input("enter the section you are studying, ")
if section in ['a','b','c']:
    print(std_class, section)
else:
    raise(data_exceptoin("invalid section"))
