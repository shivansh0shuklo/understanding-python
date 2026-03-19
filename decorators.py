# def outer_funtions(msg):
#     # message = msg##hee  message is a free variable 

#     def inner_function():
#         print(msg)
#     return inner_function

# hi_func = outer_funtions('hi')
# bye_func = outer_funtions('bye')
# hi_func()
# bye_func()

# a decorator is just a functions that takes other function as an argument and adds some kind of funcinality to it and return another function all of this without altering the source function which you passed as an arguement



def decorator(original_function):
    def inner_func(*a,**k):
        print("this executed this before {}".format(original_function.__name__))
        return original_function(*a,**k)
    return inner_func

##defining decorators as class -->
# class decorator(object):
#     def __init__(self,original_function):
#         self.original_function = ori           ginal_function

#     def __call__(self,*a,**k):
#         print("call method executed thids before {}".format(self.original_function.__name__))

#         return self.original_function(*a,**k)



@decorator
def display():
    print('display function ran')

@decorator
def display_info(name, age):
    print("display_ info run here with arguments {} {}".format(name,age))

# decorated_display = decorator(display)
# decorated_display()

display_info('jhon',35)