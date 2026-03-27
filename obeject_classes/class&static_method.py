import datetime 
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
    @classmethod
    def form_string(cls,emp_str):
        first, last,pay = emp_str.split('-')
        return cls(first,last,pay)
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday()== 6:
            return False 
        return True 
    


emp_1 = employee('riy','mishra',56000)
emp_2 = employee('shivansh', 'shukla' ,70000)

# emp_1.set_raise_amt(1.05)
# print(employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)



"""  #CLASS METHOD AS ALTERNATICE CONSTRUCTORS """
#- we can use these class methods in order to provide multiple ways of creating our objects
# emp_str_1 = 'jhon-max-700000'
# emp_str_2 = 'shivansh-max-300000'
# first,last,pay = emp_str_1.split('-')
# # new_emp_1 = employee(first,last,pay)
# new_emp_1 = employee.form_string(emp_str_2  )
# print(new_emp_1.email)
# print(new_emp_1.pay)





""" STATIC CLASS """ 
#is just anyother regular function we include them in class because they have some logical connection with the class 

my_date = datetime.date(2016,7,11)
print(employee.is_workday(my_date))
print(employee.apply_raise(emp_1))
