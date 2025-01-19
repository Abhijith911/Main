# (c) Find the result of an expression Y= ax+3b-8c / (3-2x)

print("\nFind the result of the expression Y= (ax+3b-8c)/(3-2x)")

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: ")) 
c = float(input("Enter the value of c: "))  
x = float(input("Enter the value of x: "))

numerator = (a * x) + (3 * b) - (8 * c)

denominator = 3-(2 * x)

result = numerator / denominator 
 
print(result)