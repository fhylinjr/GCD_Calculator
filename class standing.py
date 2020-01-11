def class_standing(c):
    if c<0:
        print('Put in requiered credit.')
    elif c>=0 and c<7:
        print('You are a freshman.')
    elif c>=7 and c<16:
        print('You are a sophomore.')
    elif c>=16 and c<26:
        print('You are a junior.')
    else:
        print('You are a senior.')
    
