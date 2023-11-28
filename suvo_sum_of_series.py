# sum of series
## 1-3+5-7+9-11.....
n=int(input("Enter a number : "))
sum=0
c=0

for i in range(1,n+1,2):
    if c%2==0:
        sum+=i
        print(f"+{i}",end="")
    else:
        sum-=i
        print(f"-{i}",end="")
    c+=1

print("\n")    
print(sum)
