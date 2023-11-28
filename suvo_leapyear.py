
starting_year=int(input("enter starting year "))
ending_year=int(input("enter ending year "))

print("leapyear - ",end=" ")

for year in range(starting_year,ending_year+1):
    if year%4==0 and year%400==0 or year%100!=0:
        print(year,end=" ")
