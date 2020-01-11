class Animals:
    def __init__(self):
        Name=''
        numLimbs=''
        habitat=''
        sound=''
        favFood=''

    def setName(self,Name):
        self.Name=Name

    def setnumLimbs(self,numLimbs):
        self.numLimbs=numLimbs

    def sethabitat(self,habitat):
        self.habitat=habitat

    def setsound(self,sound):
        self.sound=sound

    def setfavFood(self,favFood):
        self.favFood=favFood

    def getName(self):
        return self.Name

    def getnumLimbs(self):
        return self.numLimbs

    def gethabitat(self):
        return self.habitat

    def getsound(self):
        return self.sound

    def getfavFood(self):
        return self.favFood

    def getBio(self):
        print('I am a/an ', self.Name)
        print('I have ',self.numLimbs,' limb(s).')
        print('I live in a/an ',self.habitat)
        print('This is the sound I make: ',self.sound)
        print('I like to eat ',self.favFood)

horse=Animals()
horse.setName('Pig')
horse.setnumLimbs('4')
horse.sethabitat('style')
horse.setsound('snort')
horse.setfavFood('oat')

duck=Animals()
duck.setName('duck')
duck.setnumLimbs('2')
duck.sethabitat('pond')
duck.setsound('quack')
duck.setfavFood('seaweed')

print(horse.getBio())
print(duck.getBio())

'''print(horse.getName())
print(horse.getnumLimbs())
print(horse.gethabitat())
print(horse.getsound())
print(horse.getfavFood())'''

