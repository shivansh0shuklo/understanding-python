person = {'name':'jane','age':23}
# sentence = "my name is {0} and i am {1} years old".format(person['name'],person['age'])
# sentence = "my name is {0[name]} and i am {1[age]} years old".format(person,person)
# entence = "my name is {0[name]} and i am {0[age]} years old".format(person)


#list string formating
# l = ['jhon',25]
# sentence = "my name is {0[0]} and i am {0[1]} years old".format(l)
# print(sentence)


# tag = 'hi'
# text = 'this is a headline'
# sentence = '<{0}>{1}</{0}>'.format(tag,text)
# print(sentence)




# class person():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# p1 = person('jack','33')
# sentence = 'my name is {0.name} and i am {0.age} year old'.format(p1)
# print(sentence)






#passing keywords into placeholder
# sentence = 'name is {name} age is {age} years old'.format(name = 'sujan',age='45')
# print(sentence)




# #unpacking the dictionary into formate and it willl the keyword to use 
# person = {'name':'jin','age':24}
# sentence  = 'my name is {name} and i am {age}years old'.format(**person)
# print(sentence)


# #formating numbers
# for i in range(0,11):
#     # sentence = "the value is {}",format(i)
    # sentence = "the value is {:03}".format(i)#will now be written as 000 001 002 003 004 005.............010

    # print(sentence)





# {:} # this : was there to specify extra informations like number of zeros and no of decimal places

# pi = 3.1459265
# sentence = 'pi ia eaual to {:.3f}'.format(pi)
# print(sentence)




##something extra

# sentence = '1 mb is equal to {:,.2f} bytes'.format(100**2)### the ':,.2f' the comma or , will tell to print out the number with the comma included like 10,000 instead of 10000 and .2f just tell for the number of decimal places
# print(sentence)



import datetime
my_date = datetime.datetime(2016,9,24,12,30,45)

# sentence = '{:%B %d, %Y}'.format(my_date)# from the  website for foramting options month --> %B and day -->%d and year --> %Y
# print(sentence)


#complex formating
sentence = '{0:%B %d,%Y} the day of the week is - {0:%A} and the day of the year is - {0:%j}'.format(my_date)
print(sentence)