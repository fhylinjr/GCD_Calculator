import random
def Pshootout():
    print('Hello there!, Welcome to the Penalty Shootout Game!')
    diffmode=int(input('Select difficulty mode, Enter 1 for easy mode and 2 for hard mode: '))
    print('There are several directions to place your kick.')
    print('They are represented as TL-TopLeft, ML-MiddleLeft, BL-BottomLeft, TM-TopMiddle, M-Middle, BM-BottomMiddle, TR-TopRight, MR-MiddleRight, BR-BottomRight')
    print('As you select your spot the computer(goalie) would randomly guess a spot to attempt a save')
    print('Goodluck!!!')
    print()
    scored=0
    saved=0

    for n in range(5):
        playerOption=['TL','ML','BL','TM','M','BM','TR','MR','BR']
        goalie=random.choices(playerOption,k=6)
        shot=input('Select where you would like to shoot (TL, ML, BL, TM, M, BM, TR, MR or BR): ')
        if playerOption.count(shot)==0:
            print('You entered wrong key. You shot wide away from goal.')
            saved+=1

        if diffmode==1:
            if playerOption.count(shot)!=0:
                if goalie[0]==shot or goalie[1]==shot or goalie[2]==shot:
                    print('Goalie stopped your shot. Too Bad')
                    saved+=1
                elif goalie[0]!=shot and goalie[1]!=shot and goalie[2]!=shot:
                    print('You scored! Nice Try!')
                    scored+=1
            print('Your score is: ',scored,'-',saved)

        if diffmode==2:
            if playerOption.count(shot)!=0:
                if goalie[0]==shot or goalie[1]==shot or goalie[2]==shot or goalie[3]==shot or goalie[4]==shot or goalie[5]==shot:
                    print('Goalie stopped your shot. Too Bad')
                    saved+=1
                elif goalie[0]!=shot and goalie[1]!=shot and goalie[2]!=shot and goalie[3]!=shot and goalie[4]!=shot and goalie[5]!=shot:
                    print('You scored! Nice Try!')
                    scored+=1
            print('Your score is: ',scored,'-',saved)
        
    if scored>saved:
        print('You won the shootout. Congrats!')
    elif scored<saved:
        print('You lost the shootout. Better luck')
            


    
    
          
