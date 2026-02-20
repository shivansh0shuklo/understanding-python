'''
Docstring for VARIABLE_SCOPE

LEGB
LOCAL , ENCLOSING, GLOBAL, BUILT-IN
'''


##global and local scope

# x = 'GOBAL X'
# def test():
#     y  = "LOCAL Y"
#     print(y)
#     print(x)
# test()
# print(y)#this is local variable and it will not print as its local to that test function block


# x  = "GLOBAL X"
# def test():
#     global x #will tell taht wwe are working with the global x variable 
#     x =  "local x"#now it will change the global x
#     print(x)
# test()
# print(x)

# x = "global x"
# def test(z):
#     x  ="local x"
#     print(z)
# test('local z')
# print(x)




##importing bultin functions
##min()
# m = min([2,4,5,9,7,8])
# print(m)
import builtins
# print(dir(builtins))
def min():
    pass
## m = min([2,4,5,9,7,8])## now it will give an w=error as it is checking in the Local scope of the function





# ##inclosing scope
# def outer():
#     x = 'outer x '
#     def inner():
#         nonlocal x ##this will now make this x act like global 
#         x = 'inner x '#if we comment out this what will happer -->
#         print(x)##if we commented out inner x then this will print outer x this is inclosing scope
#         ##it will look for the local scope of any enclosing function here it is outer function 
#     inner()
#     print(x)
# outer()
# ##basically if you  have func a inside b in function b it can h=check locally in function a for the value of the variable if it's own function b does'nt have it NOT VISA VERSA function a cannot check function b locally for the value



x  = 'global x'
def outer():
    x  = "outer x "
    def inner():
        print(x)
    inner()
    print(x)
outer()
print(x)
        