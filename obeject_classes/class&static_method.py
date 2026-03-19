class employee:
    num_of_emp = 0
    raise_amount = 1.045

    def __init__(self,first,last,pay):
        self.first  = first
        self.last = last
        self.pay = pay
        self.email = first+ '.'+ last + "@company.com"
        employee.num_of_emp+=1    
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    @classmethod
    def set_raise_amt(cls, amount):##set_raise_amont is a class method which is a class method so we are dealing with class instead of instanses
        cls.raise_amount = amount

emp_1 = employee('riy','mishra',56000)
emp_2 = employee('shivansh', 'shukla' ,70000)

# emp_1.set_raise_amt(1.05)
# print(employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)



#class method as alternatice constructors - we can use these class methods in order to provide multiple ways of creating our objects
emp_str_1 = 'jhon-max-700000'
emp_str_2 = 'shivansh-max-300000'
first,last,pay = emp_str_1.split('-')
new_emp_1 = employee(first,last,pay)
print(new_emp_1.email)
print(new_emp_1.pay)

