# ## duck typing and easier to ask for forgiveness than permission (EAFP)
# class duck:
#     def quack(self):
#         print('quack,quack')
#     def fly(self):
#         print('flap,flap')
    
# class person:
#     def quack(self):
#         print("i'am quacking like a duck")
#     def fly(self):
#         print("i'am flaping my arms")
# def quack_fly(thing):
#     # # if isinstance(thing,duck):
#     # thing.quack()
#     # thing.fly()
#     # # else:
#     # #     print('this has to be a duck')
#     # # print()
#     #EAFP
    

# d = duck()
# quack_fly(d)

# p = person()
# quack_fly(p)

