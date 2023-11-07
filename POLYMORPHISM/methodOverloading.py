class MO:
    def myFunction(self):
        print("No argument Function")
    def myFunction(self,x):
        self.x=x
        print("Function with one argument",self.x)
    def myFunction(self,x,y):
        self.x=x
        self.y=y
        print("Function with two argument",self.x,self,y)
m=MO()
m.myFunction()
m.myFunction(5)
m.myFunction(5,6)
#PYTHON DOES NOT SUPPORT METHODOVERLOADING BECAUSE PYTHON IS INTERPRETED LANGUAGE