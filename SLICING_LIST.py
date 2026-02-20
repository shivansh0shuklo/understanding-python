my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#         -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

# print(my_list[:])#a empty colon will print out everything till the end including the las t asa well
# print(my_list[::-1])


sample_url = 'http://aftermeth.com'
print(sample_url)

#reverse the url
print(sample_url[::-1])

#print without the hhtp://
print(sample_url[7:])

#print url wihout the http:// and the top level domain
print(sample_url[7:-4:])