# def hello_func():
#     pass#will not let through any error for leaving the function out blank

# print(hello_func())

# def print_function(greeting,name = 'invalid',age = 'invalid'):
#     return f"{greeting} {name}, your age is - {age}"

# a = print_func()
# print(a.upper())
# print(a.lower())

# print(print_function('hi'))





#args and kwargs usage and what are that 


# def student_info(*args , **kwargs):
#     print(args)
#     print(kwargs)

# courses = {'maths','art'}
# info  ={'name':'jhon','age':22}
# student_info(*info,**info)



month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    return year%4 == 0 and (year%100!=0 or year%400==0)

def days_in_month(year,month):

    # year 2017
    # month 2
    if not 1<= month <=12:
        return "invalid month"
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]

print(days_in_month(2017,3))