#swapping using bitwise operator
a=int(input("enter the value of a: "))
b=int(input("enter the value of b: "))
a=a^b
b=a^b
a=a^b
print(f"the value of -\n a is {a} \n b is {b}")
