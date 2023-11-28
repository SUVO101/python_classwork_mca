
def fact(number):
    f=1
    for i in range(1,number+1):
        f*=i
    return f

series=int(input("Number of terms: "))
sum=0
for i in range(1,series+1):
    sum=sum+i/fact(i)

print(f"sum of series is {sum}")
