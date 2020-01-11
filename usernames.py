def main():
    firstname=input("Enter your first name in lower case: ")
    lastname=input("Enter your last name in lower case: ")
    ashesi=firstname+"."+lastname+"@ashesi.edu.gh"
    ashesi1=firstname[0]+lastname+"@ashesi.edu.gh"
    gmail1=firstname+lastname+"2@gmail.com"
    gmail2=firstname+"123"+lastname+"@gmail.com"
    gmail3=firstname+"1"+lastname+"2@gmail.com"
    
    member=eval(input("Enter 1 if you are a student and 2 if you are a staff: "))
    if member==1:
        print(ashesi)
        print(gmail1)
        print(gmail2)
        print(gmail3)
    elif member==2:
        print(ashesi1)
        print(gmail1)
        print(gmail2)
        print(gmail3)
   