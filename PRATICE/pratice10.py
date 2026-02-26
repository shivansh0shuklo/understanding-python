#The Goal: Write a function that takes a string containing only the characters (, ), {, }, [ and ]. You must determine if the input string is valid.
def string_take():
    strings_1 =  input("enter the string: ")
    string_allowed = ['{','}','[',']','(',')']
    accept = 0
    for char in strings_1:
        if(char in string_allowed):
            accept = 1


    if(accept == 1):
        print(f"string accepted -\t {strings_1}")
    else:
        print(f"not accepted is does not contain - \t {string_allowed}")
# string_take(strings_1)
string_take()


