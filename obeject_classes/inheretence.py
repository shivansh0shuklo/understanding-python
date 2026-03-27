""" ##PYHTON CLASS INHERETENCE  """

class employee:
    raise_amt = 1.05
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.'+ last+'@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amt)

class developer(employee):
    raise_amt = 1.10
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)##this super.__init__ method will let the employee class handel those arguments
        #can be also done by -->
        # employee.__init__(self,first,last,pay)
        self.prog_lang = prog_lang

class manager(employee):
    def __init__(self,first,last,pay,employes = None):
        super().__init__(first,last,pay)
        if(employes is  None):
            self.employes = []
        else:
            self.employes = employes
    def add_emp(self,emp):
        if (emp not in self.employes):
            self.employes.append(emp)
        
    def rem_emp(self,emp):
        if(emp in self.employes):
            self.employes.remove(emp)
    def print_emp(self):
        for emp in self.employes:
            print('-->',emp.fullname())




dev_1 = developer('shivansh','shukla',900000,'java')
dev_2 = developer('rohit','mishra',40000,'pyhton')


mgr_1 = manager('sue','simth','80000',[dev_1])
# print(mgr_1.email)
# mgr_1.add_emp(dev_2)
# mgr_1.print_emp()
# mgr_1.rem_emp(dev_1)
# print(mgr_1.fullname())
# mgr_1.print_emp()
# # print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

# print(dev_1.email)
# print(dev_1.prog_lang)


##some extra built in function 
##isinstance
# print(isinstance(mgr_1,employee))
# print(issubclass(developer,employee))
# print(issubclass(manager,developer))
print(isinstance(mgr_1.first,employee))




""" ##DIFEERENCE BETWEEN ISINSTANCE AND ISSUBCLASS """

""" #ISINSTANCE(OBJECT,CLASS) """
#This checks if a specific instance (an individual object you created) belongs to a class or any class it inherited from.

""" ##ISSUBCLASS(CHILD_CLASS,PARENT_CLASS) """

print(isinstance(manager,employee))##manager is a class not a abject 
print(issubclass(manager,employee))##here IT IS JUST A SUB CLASS