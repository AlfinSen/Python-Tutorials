
def binary_to_decimal(binary):
    decimal = 0
    power = 0
    

    for digit in reversed(binary):
        if digit not in ['0', '1']:
            return "Invalid binary number"
        
        decimal += int(digit) * (2 ** power)
        power += 1
    
    return decimal

binary_num = input("Enter a binary number: ")
result = binary_to_decimal(binary_num)

if isinstance(result, str):
    print(result)
else:
    print(f"Binary {binary_num} in decimal is: {result}")
