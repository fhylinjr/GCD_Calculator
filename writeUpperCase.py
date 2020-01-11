casefile=open('case.py','r')
outputfile=open('UpperCase.py','w')
for i in casefile:
    l=i.split()
    for word in l:
            print(word.upper() , end=' ', file=outputfile)

		
casefile.close()
outputfile.close()
