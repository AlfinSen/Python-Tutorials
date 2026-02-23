income = float(input("Enter your annual income: "))

tax = 0

if income <= 250000:
    tax = 0
    print("No tax to be filed")
elif income <= 500000:
    tax = (income - 250000) * 0.05
    print("Tax rate is 5% of the amount above 250,000")
elif income <= 1000000:
    tax = (250000 * 0.05) + (income - 500000) * 0.20
    print("Tax rate is 5% + 20% on amount above 500,000")
else:
    tax = (250000 * 0.05) + (500000 * 0.20) + (income - 1000000) * 0.30
    print("Tax rate is 5% + 20% + 30% on amount above 1,000,000")

net_income = income - tax

print("\n ------RESULT--------")
print("Income Tax: ", tax)
print("Net Income: ", net_income)
