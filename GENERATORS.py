##yield is used to crete a generator 
import random
import datetime

##a generatos can generate one at a time the values of the functions 

##we can use the for loop for generators to generate the values 
#can be callled as a lazy function as it return one value at a time
##it stores one value at a time 
##memory efficient
##they starts immidiatly rather than waiting for thwe whole block of code to generate and then  execute 

# def square(nums):
#     for i in nums:
#         yield i*i#the function pauses here 


# my_nums = square([1,2,3,4,5])
# print(my_nums)
# print(next(my_nums))#output for 1 
# print(next(my_nums))#output for 2
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))


#using loop
# for num in my_nums:
#     print(num)


#by converting generator into list first
# print(list(my_nums))


#list comprehensioons## will lose the advantage of memory
# my_nums = (x*x for x in [1,2,3,4,5])
# print(list(my_nums))



