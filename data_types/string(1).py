# message = 'hello world'
# print(message.count('hello'))
# print(message[2:])

# all the functions that are usefull
import string
#we cant use single qutoes inside single qutoes to 
# tackel this we will use '\' to just tell the compiler to include  the single qutoes
# print('hello\'hi')

# a = message.replace("hello","hi")
# print(a)

greet = "hello"
name = "hamel"
# # message = greet +', ' + name 
# # print(message)

# #formated string
# #place holder
# # 1 
# # message  = '{} {} welcome!'.format(greet,name)
# # 2
# # message = f'{greet},{name}.welcome'

# print(message)


# print(help(str.lower))



##speial funtions ##EXTRA NOTES
##THE COUPLE DUO maketrans()and translate()
text = "heloo, how are you?"
remove = str.maketrans("he","12","o")#maketrans("ab","12","x")#change a --> 1 & b-->2 and remove all x
new_text = text.translate(remove)##the worker which actually does the work 
print(new_text)