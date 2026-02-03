# courses = ['history','math','physics','computer']
courses_2=['art','education']
# print(courses[0:2])#will include 0 index but will not include the 2 index
# print(courses[:2])
# print(courses[2:])
# print(courses[0:-2])


# append()#will add the second list as a list not the values of the second list into the first list
# courses.append(courses_2)
# print(courses)#will append the value at the end on the list

#insert()#same as append but you can insert the vale at any places 
# courses.insert(-2,'art')
# print(courses)

# courses.insert(0,courses_2)#will add the list as a whole into the fist list
# print(courses[0][0])

#extend()#will add the value from second list
# courses.extend(courses_2)
# print(courses)

# how to remove the value
# courses.remove('math')
# print(courses)

#pop()#will remove the value and return it also

# popped = courses.pop()
# print(popped)
# print(courses)


#reverse()#will reverse
# courses.reverse()
# print(courses)

#sort()#to sort out the in ascendind order
# courses.sort()
# print(courses)
nums = [1,2,6,1,5]
# nums.sort()
# print(nums)

# courses.sort(reverse=True)
# nums.sort(reverse=True)
# print(courses)
# print(nums)


# #sorted()#will return the sorted list does not change in the original string
# a =sorted(nums)
# print(a)


#min max and sum
# print(min(nums))
# print(sum(nums))
# print(max(nums))

courses = ['history','math','physics','computer']

# print(courses.index("art"))
#for true false results we use 
# print('math'in courses)#will print the true and false 


# for item in courses :
#     print(item)

#enumerate ()#fr accesing the index as well as the value too innenumerate functions
# for index, course in enumerate(courses,start = 1):
#     print(index,course)


#list 
# courses_str = '..  '.join(courses)
# new_list = courses_str.split('.  ')
# print(courses_str)
# print(new_list)

#tuples
#inmutable 
# list_1 = ['history','math','physics','computer']
# list_2 = list_1
# print(list_1)
# print(list_2)

# list_1[0] = 'art'
# print(list_1)
# print()

# tuple_1 = ('history','maths','physics','computer')
# tuple_2 = tuple_1

# print(tuple_1)
# print(tuple_2)

# tuple_1[0] = 'art'
# print(tuple_1)
# print(tuple_2)

 #sets - values that are unordered and have no duplicates
 #curley brases are and order changes with each execution used to remove dublicate values and chek the vaues as well
 #you can check the values if they exists or not and sets are optimize for this
cs_course = {'history','math','physics','math','computer'}
art_course = {'history','math','art','design'}
print('math' in cs_course)
print(cs_course.intersection(art_course))#which elemnt are common 
#they can also fnd out what values they share and dont share with otheer sets
print(cs_course.union(art_course))
#empty sets tuples and list 
empty_tuple = ()
empty_tuple = tuple()
empty_lsit  = []
empty_list = list()
empty_sets =  {}
empty_sets = set()

