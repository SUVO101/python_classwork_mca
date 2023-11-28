series=int(input("Number of terms: "))
sum=0
str1=""
f=1
for i in range(1,series+1):
    f*=i
    sum=sum+i/f
    str1+=str(i)+"/"+str(f)+"!"

print(f"sum of series is {sum}")
print(f"\n{str1}  {sum}")