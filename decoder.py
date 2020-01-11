def decoder():
    dec1=int(input("Enter code for first character: "))
    d1=chr(dec1)
    dec2=int(input("Enter code for second character: "))
    d2=chr(dec2)
    dec3=int(input("Enter code for third character: "))
    d3=chr(dec3)
    dec4=int(input("Enter code for fourth character: "))
    d4=chr(dec4)
    dec5=int(input("Enter code for fifth character: "))
    d5=chr(dec5)
    
    d=[d1,d2,d3,d4,d5]
    for i in d:
        print(i, end="")
        
    