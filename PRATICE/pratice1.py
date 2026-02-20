#Q the question is to loop throug the list and find the average and see who is passed or who is not 
#>= 60 pass and <60 is fail print max and min also not using max() or min() functions 
grades = [85, 42, 78, 92, 55, 60]
sum  = 0
for i in grades:
    if i>=60:
        print(i,"pass")
    else:
        print(i,"fail")
    sum += i
print('average is -',sum/len(grades))
max = grades[0]
min = grades[0]
for score in grades:
    if min>score:
        min = score
    if max<score:
        max = score
print("max is -",max)
print('min is - ',min)

