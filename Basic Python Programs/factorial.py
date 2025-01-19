num = int(input(f"\nEnter a number: "))
if num == 0:
    print(f"The factorial of {num} is 1")

fact = 1
i = 1
while i < num + 1:
    fact= fact * i
    i = i+1
print(f"The factorial of {num} is {fact}")   