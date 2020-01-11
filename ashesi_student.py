class AshesiStudent:
    '''set_first_name(first_name_arg):
        first_name=first_name_arg #the class field is first_name'''
    def __init__(self, first_name, last_name, age, height, complexion, nationality, major, gpa):#init is an initializer or constructor for the class based on your object
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.height=height
        self.complexion=complexion
        self.nationality=nationality
        self.major=major
        self.gpa=gpa

    '''def set_first_name(self, first_name):
        self.first_name=first_name
    def set_last_name(self, last_name):
        self.last_name=last_name
    def set_age(self, age):
        self.age=age
    def set_height(self, height):
        self.height=height
    def set_nationality(self, nationality):
        self.nationality=nationality
    def set_major(self, major):
        self.major=major'''

    '''def get_first_name(self):
        return self.first_name
    def get_last_name(self):
        return self.last_name
    def get_full_name(self):
        return self.first_name + self.last_name
    def get_age(self):
        return self.age
    def get_height(self):
        return self.height
    def get_nationality(self):
        return self.nationality
    def get_major(self):
        return self.major'''

ernest=AshesiStudent("Ernest","Opoku",22,"5ft 8in","Dark","Ghanaian","Computer Science",3.67)
'''ernest.set_first_name("Ernest")
ernest.set_last_name("Opoku")
ernest.set_age("22")
ernest.set_height("5ft 8 in")
ernest.set_nationality("Ghanaian")
ernest.set_major("Computer Science")
print(ernest.get_first_name())
print(ernest.get_last_name())
print(ernest.get_full_name())
print(ernest.get_age())
print(ernest.get_height())
print(ernest.get_nationality())
print(ernest.get_major())
print(ernest.major,ernest.age)'''
if ernest.gpa>=3.6 and ernest.gpa<3.7:
    ernest.honors="Cum Laude"
elif ernest.gpa>=3.7 and ernest.gpa<3.8:
    ernest.honors="Magna Cum Laude"
elif ernest.gpa>=3.8 and ernest.gpa<=4.0:
    ernest.honers="Summa Cum Laude"

print(ernest.first_name)
print(ernest.last_name)
print(ernest.first_name+" "+ernest.last_name)
print(ernest.age)
print(ernest.height)
print(ernest.complexion)
print(ernest.nationality)
print(ernest.major)
print(ernest.honors)

