#creating simple classes
#logically group the data and functions to be reused or built upon


#classs is a blueprint 
# class Employee:
#     pass
# emp_1  = Employee()##unque instance 
# emp_2 = Employee()
# print(emp_1)
# print(emp_2)

# #giving the attributes
# emp_1.first = 'shivansh'
# emp_1.last = 'shukla'
# emp_1.email = 'shivansh2080@gmail.com'
# emp_1.pay  = 300000

# emp_2.first = 'Riy'
# emp_2.last = 'mishra'
# emp_2.email = 'Riy2080@gmail.com'
# emp_2.pay  = 700000


# print(emp_1.email)
# print(emp_2.email)


class Employee():
    def __init__(self,first,last,pay):##initialize = __init__
        self.first  = first##attributes of the class
        self.last = last
        self.pay = pay
    def full_name(self):
        return '{} {}'.format(self.first,self.last)



emp_1  = Employee('shiavnsh','shukla',20000)##unque instance 
emp_2 = Employee('riy','mishra',80000)

print(emp_1)
print(emp_2)
print(emp_1.full_name())
print(emp_2.full_name())

emp_1.full_name()##these both are same
print(Employee.full_name(emp_1))