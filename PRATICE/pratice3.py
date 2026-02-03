#Q coordinate traker(tuples & list)

#1. loop through the list of tuples 

location = [(10,20),(35,40),(5,15)]
for cord in location:
    print(cord)

#2. for each coordinate , calculate the sum of x and y 

sum_x = 0
sum_y=0
for i in range(len(location)):
    for j in range(2):
        if i%2 == 0:
            sum_x+=location[i][j]
        else:
            sum_y+=location[i][j]
print(f'the sum of x coordinate is - {sum_x} and the sum of the y coordinate is -{sum_y}')

#point sum of the individual points

for i in range(len(location)):
    sum_cord = 0
    for j in range(len(location)-1):
        sum_cord+=location[i][j]
    print(f'Point {i}: sum is {sum_cord}')