def march(numb):
    return 'The ants go marching ' + numb + ' by ' + numb + ','

def activity(action):
    return 'The little one stops ' + action + '\n'

def lyrics(numb,action):
    p=march(numb)+'hurrah!'*2+'\n'
    q=p*2+march(numb)+'\n'+activity(action)
    return q

def main():
    numbers=['one','two','three']
    actions=['suk his thumb','tie his shoe','eat gari']
    for i in range(3):
        print(lyrics(numbers[i],actions[i]))

main()
