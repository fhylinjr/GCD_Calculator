def ucencoder():
    alph=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    message=input("Enter your message: ")
    key=int(input("Enter your key: "))
    for i in alph:
        code=alph[i+key], end=""
        return code
    
    