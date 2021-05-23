
class Pets:
    name = ''
    breed = ''
    no_legs = 0
    def eat(self):
        print("Eating..............",self.name)


class Cat(Pets):
    def meaw(self):
        print("cat says meaw")

class Birds(Pets):          #class defnition
    def fly(self):
        print(self.name)
        print("Bird is flying")
        print("Flyin implies freedom")

# hiding all the complexities is known as abstraction.
#encapsulation 
class Dog(Pets):          # this is a class
    height = ''
    def show(self):
        print("The details of the dog are ",self.name,self.breed, self.height,self.no_legs)
    def bark(self):
        print(self.name," Dog is barking...")

# dog1 = Dog()        # dog1 is called as object
# dog1.name = 'hello'
# dog1.breed = 'xyz'
# dog1.height = 10.4
# dog1.no_legs = 4
# bird1 = Birds()
# bird1.name = "pintu"
# print(bird1.fly())
# bird2 = Birds()
# bird2.name = "raju"
# bird2.fly()
# dog1.bark()
# dog1.show()


obj  = Dog()
obj.name = "dog"
obj.eat()
obj = Cat()
obj.name = "cat"
obj.eat()

