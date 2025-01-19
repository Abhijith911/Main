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
        