
def square_root(number):
    if number < 0:
        return "Square root of negative number is not defined"
    
    if number == 0:
        return 0
    

    guess = number / 2
    tolerance = 0.00001
    
    while True:

        new_guess = (guess + number / guess) / 2
        

        if abs(new_guess - guess) < tolerance:
            break
        
        guess = new_guess
    
    return new_guess

number = float(input("Enter a number to find its square root: "))
result = square_root(number)

if isinstance(result, str):
    print(result)
else:
    print(f"Square root of {number} is approximately {result:.5f}")
