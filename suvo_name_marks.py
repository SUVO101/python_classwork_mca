# write a python prohgram that uses class to store the name and marks of the 
# students and display it.

class student:
    def __init__(self,name):
        self.name=name
        self.marks=[]
    def entermarks(self):
        for i in range(3):
            mark=int(input("enter the marks of %s in subject %d " %(self.name,i+1)))
            self.marks.append(mark)
    def display(self):
        print(f"{self.name} got {self.marks} ")
        
obj=student("suvo")
obj.entermarks()
obj.display()