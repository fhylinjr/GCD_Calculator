def main(temp):
        print("Will you like to convert your final temperature to celcius or fahrenheit\nEnter 1 for celsius or 2 for fahrenheit: ")
        reply=int(input())
        if reply==1:
            return((5/9)*(temp - 32))
        elif reply==2:
            return((9/5)*temp+32)
        else:
            print("You did not take a valid choice")

