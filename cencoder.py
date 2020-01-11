def cencoder():
    message=input("Enter your message: ")
    ckey=int(input("Enter your key: "))
    for i in message:
        print(chr(ord(i)+ckey), end="")
    
def decoder():
    message=input("Enter your message: ")
    ckey=int(input("Enter your key: "))
    for i in message:
        print(chr(ord(i)-ckey), end="")
