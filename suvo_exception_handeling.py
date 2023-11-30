try:
    n=int(input("enter the numenator: "))
    d=int(input("enter the demenator: "))
    ans=n/d
    print("quotient: ",ans)
except ZeroDivisionError:
    print("denominator can not be zero.")
except KeyboardInterrupt:
    print("key board interrupt error")
else:
    print("successful")
finally:
    print("clean up")