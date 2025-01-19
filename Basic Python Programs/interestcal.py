
# (c) Program to Calculate Simple Interest

print("\nProgram to Calculate Simple Interest\n")

Principal = float (input("Enter the principal amount: "))

Rate = float (input("Enter the rate of interest: "))

Years = float (input("Enter the number of years: ")) 

simpleInterest = (Principal * Years * Rate) / 100

print (f"The simple interest is: {simpleInterest}")
