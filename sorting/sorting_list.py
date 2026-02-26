# li  = [9,1,2,3,8,6,4,5]

# s_li  = sorted(li)#for this method the original is not sorted out instead the new sorted lis is formed
# print("sorted variable:\t",s_li)
# li.sort()#for this the original list will be sorted uot
# print("original variable :\t",li)


#for decending order 

# s_li = sorted(li,reverse=True)
# print("sorted : \t", s_li)


# li = [-6,-5,-7,1,2,3]
# s_li = sorted(li,key=abs)#abs is absolute value fuunction it will sort them in basis of absolute value
# print(f'list\t {s_li}')



class employee():
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    def __repr__(self):
        return '({},{},s{}'.format(self.name,self.age,self.salary)
from operator import attrgetter

e1  = employee('carl',37,70000)
e2  = employee('saran',47,73000)
e3  = employee('john',40,80000)


employees = [e1,e2,e3]

def e_sort(emp):
    return emp.name


# s_employees = sorted(employees,key=e_sort)
s_employees = sorted(employees,key=attrgetter('age'))#using an module
print(s_employees)