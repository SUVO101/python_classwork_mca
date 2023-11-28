
# define factorial function
def factorial(num):
    f=1
    for i in range(1,num+1):
        f=f*i
    return f

# define peterson function
def peterson(number):
    sum1=0
    copy_number=number
    while number>0:
        rem= number % 10
        sum1+=factorial(rem) # call the factorial() function
        number=number//10
    if(copy_number==sum1):
        return(f"{copy_number} is peterson number")
    else:
        return (f"{copy_number} is not peterson number")
    
number=int(input("Enter a number to check wheather the input is peaterson or not ? "))
print(peterson(number))


    
    
