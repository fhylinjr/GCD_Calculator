countfile=open('filename.py','r')
a=countfile.read()
print(a)

print('The number of characters in your file is: ',len(a))

print('The number of words in your file is: ',len(a.split()))

sentences=len(a.split('.'))-1
print('The number of lines/sentences in your file is: ',sentences)
