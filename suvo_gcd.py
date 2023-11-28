# gcd of two integers uisng recursion

def gcd(a,b):
    rem=a%b
    if rem==0:
        return b
    else:
        return gcd(b,rem)

a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
print(gcd(a,b))