def decimal_to_binary(number):
    sum,i=0,0
    while number>0:
        rem=number%2
        sum+=rem*(10**i)
        number=number//2
        i+=1
    return sum

number=int(input("Enter a decimal number : "))
print(f"binary of {number} is {decimal_to_binary(number)}")

