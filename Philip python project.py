import random #This imports the random module
numberofguesses=0 #This takes note of the fact that no try has yet been made

print("Hi there!, What's your name?") #Prompting the user to enter name
name=input() #Reading the information the user has entered and storing it in a variable called name

number=random.randint(1,15) #this generates a random number the user is expected to guess within a defined range
print(name+", the number I am thinking of is between 1 and 15") #This infroms the user of the range in which he can be guessing
determine = " " #This line initialises the value of the variable determine to ensure that the loop condition is verified the first time the code runs

while ((numberofguesses<3) and determine!="END"): #user has a maximum of 3 attempts to guess correctly
    print("Try guessing. ")
    determine=input() #This temporarily holds the input from the user in a string called determine
    if determine.isdigit(): #We check if the variable determine is a digit, and if so, we proceed to evaluate it's value
        guess=int(determine) #Since we are sure that the variable determine is a digit, we can cast it to an interger
    
        numberofguesses=numberofguesses+1
        #this section of the code checks if the user's guess is correct
        if guess>number:
            print(name+" the number is too high. \n Type END to quit.") #informs the user to input a lower number or quit
        if guess<number:
            print(name+" the number is too low. \n Type END to quit") #informs the user to input a higher number or quit
        if guess==number:
            break #the loop exits if the user guesses correctly
    else: #If the value of determine is not a digit, then we verify if it is a string that ends the loop condition
        continue #We exit the loop, and strart all over again
if numberofguesses<3: #checks if the user has not used up all attempts
    print("Oh " + name+ " why did you quit? See you another time") #this informs the user why he/she quit
else:
    if guess==number: #confirms that user's input equals random generated number
        numberofguesses=str(numberofguesses) #this allows the variable to be used and printed in a string format
        print("Congratulations "+name+"!! You have guessed the number in "+numberofguesses+" attempt(s)") #this prints the user was successful
    if guess!=number: #confirms that user's input does not equal random generated number
        number=str(number) #this allows the variable which allowed a random number generation be used and printed in a string format
        print("Wrong "+name+ "! How unlucky, the number I thought of was "+number) #this prints the user was unsuccessful
