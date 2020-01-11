Age=int(input("Enter your age"))
if Age>=0 and Age<=1:
    print("You are a baby")
elif Age>1 and Age<=3:
    print("You are a toddler")
elif Age>3 and Age<=4:
    print("You are a toddler and are in preschool")
elif Age>=5 and Age<10:
    print("You are in grade school")
elif Age>=10 and Age<18:
    print("You are a teenager")
else:
    print("You are an adult")