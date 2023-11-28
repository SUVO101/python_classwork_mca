# decimal to binary
def decimal_to_binary(number):
    str1=""
    while number>0:
        rem=number%2
        str1=str(rem)+str1
        number=number//2
    return str1

number=int(input("Enter a decimal number : "))
print(f"binary of {number} is {decimal_to_binary(number)}")
