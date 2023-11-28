p=0
n=0
pc=0
nc=0
while True:
    number=int(input("enter a number: "))
    if number==-9999:
        break
    elif number>=0: #positive
        pc+=1
        p+=number
    elif number<0: #negative
        nc+=1
        n+=number
pos_avg=p/pc
neg_avg=n/nc
print(f"Positive Average {pos_avg}")
print(f"Negative Average {neg_avg}")
