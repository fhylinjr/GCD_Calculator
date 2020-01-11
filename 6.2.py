def mode():
    lst=[1,2,3,4,4.99,5,6,6,7]
    tally=1
    for i in lst:
        fmod=lst.count(i)
        if fmod > tally:
            tally = fmod
            print(i)
        else:
            tally = tally
            
        
    
        
mode()
