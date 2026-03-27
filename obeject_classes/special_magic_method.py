class employee:
    raise_amt = 1.04
    def __init__(self,first,last,pay):#this '__' double underscore is called dunder the actual word is called dunder
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.'+ last+'@gmail.com'
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amt)
    """ ##TWO SPECIAL METHODS WE SHOULD ALWAYS USE  """
    def __repr__(self):##repr an anbiguios representation representaion of the object and should be used for the logging and documentaion 
        return "employee('{}','{}','{}')".format(self.first,self.last,self.pay)    

    def __str__(self): ##readable representaion of the objects  
        return '{} - {}'.format(self.fullname(),self.email)
    def __add__(self,other):
        return self.pay + other.pay
    def __len__(self):
        return len(self.fullname())
    



emp_1  = employee('shiavnsh','shukla',20000)##unque instance 
emp_2 = employee('riy','mishra',80000)
  

""" #CALLING THE REPR AND STR """
# print(str(emp_1))##calling the str
# print(repr(emp_1))##calling the repr
#SECOND METHOD OF DOING THIS        
# print(emp_1.__repr__())
# print(emp_1.__str__())




# print(1+2)#this + can be accessed with the dunder add method as well
# print(int.__add__(1,2))

# print(emp_1+emp_2)





# print(len('test'))
# print('test'.__len__())
print(len(emp_1)) 