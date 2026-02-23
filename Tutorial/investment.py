initial_amount = float(input("Enter the initial investment amount: "))
interest_rate = float(input("Enter the annual interest rate (in %): "))
years = int(input("Enter the number of years: "))

amount = initial_amount

print("\nYear\tAmount")

for year in range(1, years + 1):
    amount = amount + (amount * (interest_rate / 100))
    print(f"{year}\t{amount:.2f}")
