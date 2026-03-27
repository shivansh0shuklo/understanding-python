import sqlite3
from employee import Employee
con = sqlite3.connect('employee.db')
c = con.cursor()
# c.execute("""CREATE TABLE employee(
#             FIRST TEXT,
#             LAST TEXT,
#             PAY INTEGER       
#           )""")

def insert_emp(emp):
    with con:
        c.execute("INSERT INTO employee VALUES(:FIRST,:LAST, :PAY)",{'FIRST':emp.first,'LAST':emp.last,'PAY':emp.pay})

def get_emp_by_name(lastname):
    c.execute("SELECT * FROM employee WHERE LAST=:LAST",{'LAST':lastname})
    return c.fetchall()

def update_pay(emp,pay):
    with con:
        c.execute(''' UPDATE employee SET PAY = :PAY
                  WHERE FIRST = :FIRST AND LAST = :LAST''',
                  {'FIRST':emp.first,'LAST': emp.last,'PAY':pay})
        
def remove_emp(emp):
    with con:# if we want to execute something we will use the with 
        c.execute('DELETE FROM employee WHERE FIRST = :FIRST AND LAST = :LAST',
                  {'FIRST':emp.first,'LAST':emp.last})


emp_1 = Employee('after','meth',300000)
emp_2 = Employee('test','hello',900000)

# insert_emp(emp_1)
# insert_emp(emp_2)
emps = get_emp_by_name('meth')
print(emps)
update_pay(emp_2,950000)
remove_emp(emp_1)
print(c.execute(' SELECT * FROM employee'))
print(c.fetchall())
print("\n")
remove_emp(emp_2)
print(c.execute(' SELECT * FROM employee'))
print(c.fetchall())

con.close()


# print(emp_1.first)
# print(emp_1.last)
# print(emp_1.fullname)
# print(emp_1.pay)



""" #adding data to our table  """
# c.execute("INSERT INTO employee VALUES(?,?,?)",(emp_1.first,emp_1.last,emp_1.pay))
# con.commit()

# c.execute("INSERT INTO employee VALUES(:FIRST,:LAST, :PAY)",{'FIRST':emp_2.first,'LAST':emp_2.last,'PAY':emp_2.pay})
# con.commit()



""" #TWO WAYS OF USING THE PLACEHODESRS """
# c.execute("SELECT * FROM employee WHERE LAST=?",('meth',))
# print(c.fetchall())
# con.commit()

# c.execute("SELECT * FROM employee WHERE LAST=:LAST",{'LAST':'MISHRA'})
# print(c.fetchall())
# con.commit()
# con.close()