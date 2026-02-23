number = int(input("Enter a number: "))
temp = number
sum_of_digits = 0
num_digits = len(str(number))

while temp > 0:
    digit = temp % 10
    sum_of_digits += digit ** num_digits
    temp //= 10

if number == sum_of_digits:
    print(f"{number} is an Armstrong number")
else:
    print(f"{number} is not an Armstrong number")
