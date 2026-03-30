import numpy as np

""" #USING ARRAY """
## we will use list like this because of two resons first reons is contiguous memory and second one math logics

# array = np.array([1,2,3,4])
# print(array)
# array = array*2
# print(array)
# print(type(array))




""" ##MULTIDIMENSIONAL ARRAY """
#ndim to check the dimensionality of the data give 
# ['a','b'] is one dimension
#'a' is 0th dimension
#[['a'],['b']] is 3 dimension
# array = np.array(['a','b'])
# array = np.array([[['a','b','c'],['g','h','i']],
#                   [['ab','bn','g'],['h','j','k']]])

# print(array[0,0,0])## multidimesional indexing (faster)
# print(array[0][0][0])## chain indexing (slower than the multidimensional indexing)


# word = array[0,0,0] + array[0,1,2] + array[1,1,2] 
# print(word)




""" ##SLICING """
# array = np.array([[1,2,3,4],
#                   [5,6,7,8],
#                   [9,10,11,12],
#                   [13,14,15,16]])
#array[start:end:step]#ending index is exclusive 
# print(array[::-2])#row selection
# print(array[:,0:1])#selecting all rows and then selecting coloum 0
# print(array[:,1::2])
# print(array[2:,2:])




""" ##ARITHMETIC """

""" #scalar arithmetic """
array =  np.array([1,2,3])
# print(array+1)
# print(array/4)
# print(array**5)
# print(array-2)
# print(array*3)



""" #vectorised arithmetic funcs """
# array =  np.array([1.01,2.5,3.99])
# print(np.sqrt(array))
# print(np.round(array))
# print(np.floor(array))# to round back 
# print(np.ceil(array))#to round forword

# radii = np.array([1,2,3])
# print(np.pi*radii**2)#to calcultae the radii of a circle

""" #element-wise arithmetic """
# array1 = np.array([1,0,3])
# array2 = np.array  ([4,5,6])
# print(array1 + array2)
# print(array1-array2)
# np.seterr(divide='raise')
# try:
#     print(array2/array1)
# except FloatingPointError:
#     print("cannot be divided by zero sorry")
# print(array1**array2)
# print(array2*array1)

""" ##comparison operator  """

# scores = np.array([91,100,55,73,82,64])
# print(scores == 100)
# print(scores>=60)
# scores[scores<60] = 0
# print(scores)


""" ##BROADCASATING """
#BROADCASTING allows numpy to perform operations on arrays
#with different shape by virtually expanding dimensions
#so they match the larger array shape

""" #two dimension are compatible  """
#the dimensions have the same size
#or
#one of the dimensions has a size of 1
""" #we read right to left in broadcasting """
# array1 = np.array([[1,2,3,4],
#                    [5,6,7,8],
#                    [1,1,7,8],
#                    [8,9,10,11]])
# array2 = np.array([[1],[2],[3],[4]])
# print(array1.shape)
# print(array2.shape)

# print(f'\n{array1} * \n{array2} = \n{array1*array2}')

array1  = np.array([[1,2,3,4,5,6,7,8,9,10]])
array2 = np.array([[1],[2],[3],[4],[5],[7],[8],[9],[10]])
print(array1*array2)