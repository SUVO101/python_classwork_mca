def factorial(num):
    f=1
    for i in range(1,num+1):
        f=f*i
    return f

number=int(input("Enter a number to check wheather the input is peaterson or not ?"))
sum1=0
copy_number=number
while number>0:
    rem= number % 10
    sum1+=factorial(rem)
    number=number//10

if(copy_number==sum1):
    print(f"{sum1} is peterson number")
else:
    print(f"{sum1} is not peterson number")
    
    
