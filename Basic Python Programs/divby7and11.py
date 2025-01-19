num = int(input("enter the number : "))
if num % 7 == 0 and num % 11 == 0 :
    print(f"{num} is divisible by both 7 and 11 ")
elif num % 7 == 0 :
    print(f"{num} is divisible by  7 ")
elif num% 11 == 0 :
      print(f"{num} is divisible by 11 ")    
else :
      print(f"{num} is not divisible by both 7 and 11 ")   