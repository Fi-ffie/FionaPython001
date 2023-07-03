class Magari:
    def __init__(self,modelname,color,year,capacity):
        self.model = modelname
        self.mycolor = color
        self.myyear = year
        self.mycapacity = capacity
    def onyesha(self):
        print(self.model, self.mycolor, self.myyear,self.mycapacity)

#create an object
myobj = Magari("Toyota", "White",2020,"2000cc")
myobj.onyesha()
myobj = Magari("Charvolet", "Black",2020,"2800cc")
myobj.onyesha()
myobj = Magari("Mercedes", "RoyalBlue",2012,"3000cc")
myobj.onyesha()