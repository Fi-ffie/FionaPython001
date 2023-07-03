class People:
    def __init__(self,name,gender,age):
        self.myname = name
        self.mygender = gender
        self.myage = age
    def onyesha(self):
        print(self.myname, self.mygender, self.myage)
# create an object
myobj = People("Lauren Weston ", "Female", 20)
myobj.onyesha()
myobj = People("Tariq St.Patrick", "Male", 19)
myobj.onyesha()
myobj = People("Cane Tehada", "Male", 23)
myobj.onyesha()
myobj = People("Yasmine St.Patrick", "Female", 14)
myobj.onyesha()