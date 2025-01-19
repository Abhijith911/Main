x = int(input(f"\nEnter the first number: "))
y = int(input(f"\nEnter the second number: "))
z = int(input(f"\nEnter the third number: "))

if(x>y):
    if(x>z):
        print(f"\nThe largest number is {x}")
elif(y>z):
    print(f"\nThe largest number is {y}")
else:
    print(f"\nThe largest number is {z}")