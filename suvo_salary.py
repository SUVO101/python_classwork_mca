salary=float(input("enter employee salary: "))
gender=input("enter employee gender m / f ? ")
if(gender=='m'):
    bonus=salary*5/100
else:
    bonus=salary*10/100
if(salary<10000):
    bonus=salary*2/100+bonus
print(f"salary : {salary} \n gender : {gender} \n bonus : {bonus}")
    
# using nested if else

