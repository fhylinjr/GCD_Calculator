x=open('myTriples.txt','r')
total=0.0
count=0
for line in x:
       numbers=line.split(',')
       for num in numbers:
           total=total+float(num)
           count=count+1
print(total)
print(total/count)
