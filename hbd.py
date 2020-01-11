def happy():
    return('Happy birthday to you')

def singfor(friend):
    l=happy()*2 +" Happy birthday dear "+ friend+"\n"+ happy()+"\n"
    return l

def main():
    for name in ['Abena','Kweku']:
        print(singfor(name))

main()
