#write a program to check the entered STRING is symmertical or palindrom

Value = input("Enter the Value: ")

if Value == Value[::-1]:
    print("Thisis a the palindrom")
else:
    print("This is a not a palindrom")

mid = len(Value) // 2

if len(Value) % 2 == 0:
    if Value[:mid] == Value[mid:]:
        print("This is symmetrical")
    else:
        print("This is not symmetrical")
else:
    if Value[:mid] == Value[mid+1:]:
        print("This is symmetrical")
    else:
        print("This is not symmetrical")


"""Hello
ioioiuifkjdhfkldsflknf"""
