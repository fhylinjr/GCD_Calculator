Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> myfile=open('read python.py','r')
>>> myfile.readline()
'2\n'
>>> myfile.readlines()
['4\n', '6\n', '4\n', '8\n', '34\n', '6\n', '7\n']
>>> myfile.readlines(2)
[]
>>> myfile.readlines(3)
[]
>>> myfile.readline(3)
''
>>> myfile.readline(1)
''
>>> myfile.readlines(1)
[]
>>> myfile=open('read python.py','r')
>>> myfile.readlines(2)
['2\n', '4\n']
>>> myfile=open('read python.py','r')
>>> for i in range(4):
	line=myfile.readline()
	print(line)

2

4

6

4

>>> myfile=open('read python.py','r')
>>> for i in range(5):
	line=myfile.readline()
	print(line\n)
	
SyntaxError: unexpected character after line continuation character
>>> for i in range(5):
	line=myfile.readline()
	print("line\n")

	
line

line

line

line

line

>>> myfile=open('read python.py','r')
>>> for i in range(4):
	line=myfile.readline()
	print("line\n")

	
line

line

line

line

>>> rainfile=open('rainfall.py','r')
>>> outputfile=open('rainfallcm.py','w')
>>> for i in rainfile:
	values=i.split()
	print(values[0], 'had',values[1], 'inches of rain.')
	print(values[0], 'had',values[1]*2.54, 'cm of rain.',file=outputfile)

	
Akron had 25.81 inches of rain.
Traceback (most recent call last):
  File "<pyshell#34>", line 4, in <module>
    print(values[0], 'had',values[1]*2.54, 'cm of rain.',file=outputfile)
TypeError: can't multiply sequence by non-int of type 'float'
>>> outputfile=open('rainfallcm.py','w')
>>> 
>>> 
>>> 
>>> rainfile=open('rainfall.py','r')
>>> outputfile=open('rainfallcm.py','w')
>>> for i in rainfile:
	values=i.split()
	print(values[0], 'had',values[1], 'inches of rain.')
	print(values[0], 'had',int(values[1])*2.54, 'cm of rain.',file=outputfile)

	
Akron had 25.81 inches of rain.
Traceback (most recent call last):
  File "<pyshell#42>", line 4, in <module>
    print(values[0], 'had',int(values[1])*2.54, 'cm of rain.',file=outputfile)
ValueError: invalid literal for int() with base 10: '25.81'
>>> rainfile=open('rainfall.py','r')
>>> outputfile=open('rainfallcm.py','w')
>>> for i in rainfile:
	values=i.split()
	print(values[0], 'had',values[1], 'inches of rain.')
	print(values[0], 'had',float(values[1])*2.54, 'cm of rain.',file=outputfile)

	
Akron had 25.81 inches of rain.
Albia had 37.65 inches of rain.
Algona had 30.69 inches of rain.
Allison had 33.64 inches of rain.
Alton had 27.43 inches of rain.
>>> 
>>> 
>>> 
>>> rainfile=open('rainfall.py','r')
>>> outputfile=open('rainfallcm.py','w')
>>> for i in rainfile:
	values=i.split()
	print(values[0], 'had',values[1], 'inches of rain.')
	print(values[0], 'had',float(values[1])*2.54, 'cm of rain.',file=outputfile)

Akron had 25.81 inches of rain.
Albia had 37.65 inches of rain.
Algona had 30.69 inches of rain.
Allison had 33.64 inches of rain.
Alton had 27.43 inches of rain.
>>> rainfile=open('rainfall.py','r')
>>> outputfile=open('rainfallcm.py','w')
>>> for i in rainfile:
	values=i.split()
	print(values[0], 'had',values[1], 'inches of rain.')
	print(values[0], 'had',float(values[1])*2.54, 'cm of rain.',file=outputfile)
rainfile.close
SyntaxError: invalid syntax
>>> rainfile=open('rainfall.py','r')
>>> outputfile=open('rainfallcm.py','w')
>>> for i in rainfile:
	values=i.split()
	print(values[0], 'had',values[1], 'inches of rain.')
	print(values[0], float(values[1])*2.54,file=outputfile)

	
Akron had 25.81 inches of rain.
Albia had 37.65 inches of rain.
Algona had 30.69 inches of rain.
Allison had 33.64 inches of rain.
Alton had 27.43 inches of rain.
>>> rainfile=open('rainfall.py','r')
>>> outputfile=open('rainfallcm.py','w')
>>> for i in rainfile:
	values=i.split()
	print(values[0], 'had',values[1], 'inches of rain.')
	print(values[0], float(values[1])*2.54,file=outputfile)

Akron had 25.81 inches of rain.
Albia had 37.65 inches of rain.
Algona had 30.69 inches of rain.
Allison had 33.64 inches of rain.
Alton had 27.43 inches of rain.
>>> 
================ RESTART: C:/Users/phili/Desktop/Google/cm.py ================
Akron had 25.81 inches of rain.
Albia had 37.65 inches of rain.
Algona had 30.69 inches of rain.
Allison had 33.64 inches of rain.
Alton had 27.43 inches of rain.
>>> 
