#currency convertor
outputfile=open('currency1.py','w')
def currency():
    rate=[5.28,5.29,6.54]
    cedi=float(input('Enter any cedi amount you would like to convert: '))
    a=cedi*rate[0]
    b=cedi*rate[1]
    c=cedi*rate[2]
    print(cedi,' GHC is : ',a,' dollars\n' ,cedi,' GHC is : ',b,' euros\n' ,cedi,' GHC is : ',c,' pounds\n' ,file=outputfile)

outputfile.close()

