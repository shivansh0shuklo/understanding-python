class employee:
    def __init__(self,first,last):
        self.first = first
        self.last = last
    
    @property
    def email(self):
        return '{} {}@gmail.com'.format(self.first,self.last)
    
    """ THIS @property ACT AS A GETTER """
    @property 
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    """ THIS ACT AS A SETTER  """
    @fullname.setter
    def fullname(self,name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter## this uses the del keyword
    def fullname(self):
        print('deleted name!')
        self.first = None
        self.last = None

emp_1 = employee('shivansh','mishra')
emp_1.fullname = 'ROHIT SHUKLA'

print(emp_1.first)
print(emp_1.email)##IF WE WANT TO CONTINUE ACCESSING THE EMAIL AS AN ATTRIBUTE WE WILL USE THE PROPERTY DECORATER
print(emp_1.fullname)

del emp_1.fullname
print(emp_1.fullname)






##PROPERTRY DECORATOR - HELP US TO DEFINE A METHOD BUT USE THAT AS AN ATTRIBUTE

""" SETTER """ 
#THIS IS A ENTRY FUNCTION WHICH DEFINES HOW THE DATA IAS PHRASED

""" @property """
#THIS IS AOR PRIMARY FUNCTION . THIS ACTUALLY DEFINES HOW THE DATA IS PRESENTED