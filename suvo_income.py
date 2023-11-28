# calculate income tax
income=float(input("enter income : "))
if income < 250000:
    tax="no tax"
elif income >= 250000 and income < 500000:
    tax=(income-250000)*10/100
elif income >= 500000 and income < 800000:
    tax=(499999-250000)*10/100+(income-500000)*20/100
else:
    tax=(499999-250000)*10/100+(799999-500000)*20/100+(income-800000)*30/100

print(f"income : {income} tax : {tax:.2f}")
