x = int(input("Enter the number: "))

for num in range(2, x + 1):
    flag = True
    for i in range(2, int(num//2) + 1):
        if num % i == 0:
            flag = False
            break
    if flag:
        print(num)