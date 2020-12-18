class Gun:
    length = 0
    breadth = 0
    height = 0
    magzine_size = 0
    name = ""
    material = ""   
    skin = ""
    def firing(self):
        pass
    def aiming(self):
        print("Default aiming code Here!")

    def display(self):
        print(self.name," has magzine size of ",self.magzine_size)

    
class Pistol(Gun):
    def __init__(self,name):
        self.name = name
    def aiming(self):   #funcion overriding....
        print("Aiming at short range")
    
    
class Rifle(Gun):
    def __init__(self,name):
        self.name = name
    def aiming(self):
        aim_range = input("Enter the range you want to set")
        print("Aiming at ",aim_range)


class Sniper(Gun):
    def __init__(self,name):
        self.name = name

    def aiming(self):
        print("using scope to aim at the enemy")



hand_gun = Pistol("Hand gun")
hand_gun.magzine_size = 15
hand_gun.display()
awm = Sniper("AWM")
awm.magzine_size = 7
awm.firing()
awm.display()
hand_gun.aiming()
awm.aiming()
m416 = Rifle("M416")
m416.aiming()
m416.display()

        



