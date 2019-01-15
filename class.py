#!/usr/bin/env python3




class line:

    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2

        return ((x2-x1)**2 + ((y2-y1)**2))**0.5




    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2

        return (y2-y1) / (x2-x1)









coordinate1 = (3,2)
coordinate2 = (8,10)

li = line(coordinate1,coordinate2)


print(li.distance())
print(li.slope())

#------------------------------------------------------
class Cylinder:

    def __init__(self,height = 1,radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return self.height*3.14*(self.radius)**2        

        
    def surface_area(self):
        top = 3.14*(self.radius)**2
        return(2*top)+(2*3.14*(self.radius*self.height))
        
        
        
        
c = Cylinder(2,3)
print(c.volume())
print(c.surface_area())





    
#---------------------------------------------------------------
class Account:

    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account owner:  {self.owner}\nAccount balance: Bath{self.balance}'


    def deposit(self,atm):
        self.balance += atm
        print('DONE')
        

    def withdraw(self,w_atm):
        if self.balance > w_atm:
            self.balance -= w_atm
            print('withdraw accp')


        else:
            print('fuck off')



acc1 = Account('dearx',100)
print(acc1.withdraw(50))
print(acc1)
            


