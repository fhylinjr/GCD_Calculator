rainfile=open('rainfall.py','r')
outputfile=open('rainfallcm.py','w')
for i in rainfile:
    values=i.split()
    print(values[0], 'had',values[1], 'inches of rain.')
    print(values[0], 'had',float(values[1])*2.54, 'cm of rain.',file=outputfile)

rainfile.close()
outputfile.close()
