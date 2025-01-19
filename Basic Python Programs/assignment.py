# NAME   : Abhijith Santhosh
# BRANCH : ER
# ROLL NO: 1
# DATE   : 07-01-2025

# EXPT NO: 1
# Introduction to Python basics - Programmes on usage of data typesexpressions- variables and operators



# (a) Input and Display Values of Different Data Types (int, float, string anf bool) and print the values

i = int(input(f"\nEnter a integer:"))
print(i)

f = float(input(f"Enter a floating number:"))
print(f)

b = bool(input(f"Enter a boolean number:"))
print(b)

s = input(f"Enter the variable:")
print(s)




# (b) Perform Arithmetic Operations (addition, subtraction, multiplication and division)

print("Perform Arithmetic Operations\n")

num1 = float(input(f"Enter the first number:"))
num2 = float(input(f"Enter the second number:"))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")
print(f"Division: {num1} / {num2} = {division}")



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

# Exp No: 2 
# Input methods and data processing - Implementing Python programs to process input data and format output


# (a) Program to convert temperature from celcius to fahrenheit

print("\nProgram to convert temperature from celcius to fahrenheit\n")

Celsius = float(input("Enter temperature in celsius: "))
Fahrenheit = (Celsius * 9/5) + 32

print(f"{Celsius} °C is equal to {Fahrenheit} °F")



# (b) Program to Count Words in a Sentence

print("\nProgram to Count Words in a Sentence\n")

sentence = input ("Enter a sentence: ")

words = sentence.split()

wordCount = len(words)

print (f"The number of words in the sentence is: {wordCount}")




# (c) Program to Calculate Simple Interest

print("\nProgram to Calculate Simple Interest\n")

Principal = float (input("Enter the principal amount: "))

Rate = float (input("Enter the rate of interest: "))

Years = float (input("Enter the number of years: ")) 

simpleInterest = (Principal * Years * Rate) / 100

print (f"The simple interest is: {simpleInterest}")





















# Exp No 3: Control statements - Writing programs incorporating if and if-else. 

# a. Program to check if a number is positive, negative, or zero using a nested if-else statement.


num = int(input(f"Enter a number: "))
if num<0:
    print(f"The number {num} is negative")
elif num>0:
    print(f"The number {num} is positive")
else:
    print(f"The number {num} equals to zero")        



# b. Program to check a person's age group (child, teenager, adult, senior) using  if-elif-else statement.

age = int(input(f"Enter your age:\t"))
if(age<=0):
    print(f"\nYou havnt born DUDE 💀🙏🏿 ")
    exit()
if age<=12:
    print(f"\nYou are a child")
elif 13<=age<=19:
    print(f"\nYou are a teenager")
elif 20<=age<=59:
    print(f"\nYou are an adult")    
else:
    print(f" You are a senior citizen")    
        

 # c. Program to find the smallest of three numbers.


a = int(input(f"Enter the first number: "))
b = int(input(f"Enter the second number: "))

if(a<b):
    print(f"{a} is the smallest number")
else:    
    print(f"{b} is the smallest number")

