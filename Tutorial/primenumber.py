# writie a program to print prime numbers within in the range

lower = int(input("Enter the lower input of prime number: "))
upper = int(input("Enter the upper input of prime number: "))

if (lower <= 1):
    lower = 2

for i in range(lower,upper+1):
    flag = 0
    for j in range(2,i):
        if i%j==0:
            flag = 1
            break
    if flag == 0:
        print(i)
