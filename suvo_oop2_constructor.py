class Class() :
    def __init__(self,value):
        self.value=value
        print(f"inside class the value is {self.value}")

#obj=Class(15)

class Class_one:
    _var=0
    def __init__(self,a,b):
        self.value1=a
        self.value2=b
    def display(self):
        Class_one._var+=1
        print(f"the value of first parameter is {self.value1} \n the value of second parameter is {self.value2} \n the value of class variable is {Class_one._var} \n")

obj=Class_one(10, 20)
obj.display()