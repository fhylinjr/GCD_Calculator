def main():
    c=eval(input('Enter the clocked speed: '))
    s=eval(input('Enter speed limit which should not be over 145km/h: '))
    if s>145:
        print('Enter an appropriate speed limit.')
    elif c<s:
        print('Speed is legal.')
    elif c>=s and c<=145:
        f=(c-s)*50
        print('Your fine is ',f,' cedis.')
    elif c>145:
        g=((c-s)*50 +200)
        print('Your fine is ',g,' cedis.')

main()
