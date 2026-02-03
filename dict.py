#dictionary how to worl with it #Are also  called hash map in other programing language 
student = {'name':'jhon','age':25,'courses':['math','science']}
# print(student['couses'])

#get()

# print(student.get('phoen'))#get will return none value if there is not the variable in the dictionary 
#you can akso specify the defalut value if the vaue was not founded
# print(student.get('phone',1))#get(value,default_key)

#update()
student.update({'name': 'jane','age':36,'phone':'9999-999-99'})


# #print(student.get('phone','not found'))
# print(student)

#for deleate the element we will use del keyword 
# del student['age']

#for delete using pop()
#pop wil return the value that i deleted ad well
age  = student.pop('age')
print(student)
print(age)

#misclaneous
#for number of keys in the dict 
print(len(student))
#keys()
#to print out the keys in the dictionary
print(student.keys())
#values() - to print out the values of the dictionary
print(student.values())
#items() - to see both keys and vakues as well 
print(student.items())
for key,value in student.items():
    print(key,value)