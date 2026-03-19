class employee:
    raise_amount = 1.04
    num_of_emp = 0

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


emp_1 = employee('riy','mishra',56000)
emp_2 = employee('shivansh', 'shukla' ,70000)

print(emp_1.__dict__)
# print(employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

emp_1.raise_amount = 1.85

# print(emp_1.__dict__)
# print(employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)


print(employee.num_of_emp)