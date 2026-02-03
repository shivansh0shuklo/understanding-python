# from mymodule.my_module import find_index as index  #if we import this way we will not have access to the test strng in the my_module as we are only importing find_index function

# from mymodule.my_module import find_index as f,test as t
courses = ['history','math','physics','compsci']
# index = f(courses,"math")
# print(index)
# print(t)

#to import everything we will use *

# import sys
# from mymodule.my_module import *#we can't tell what came from that module 
# index  = find_index(courses,"math")
# # print(index)
# # print(test)


# #sys will import the path variables as a list 
# print(sys.path)



#appending module directory
import sys
sys.path.append("/Users/shiva/python/importng modules/mymodule")
from my_module import find_index
print(find_index(courses,"math"))



