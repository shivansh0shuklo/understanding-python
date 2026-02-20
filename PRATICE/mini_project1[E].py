##number guessing game 
import random
# random.randrange(start,stop)#number stop will not generate
# print(random.randrange(-5,11))

# random.randint(start,stop)#now the stop will be included
top_of_range = input("type a number: ")

if(top_of_range.isdigit()):
    top_of_range = int(top_of_range)
    if(top_of_range <= 0):
        print("type a number next time")
        quit()
else:
    print("please type a number next time.")
random_number = random.randint(0, top_of_range)
print(random_number)
guess = 0
while True:
    guess += 1
    input_number = int(input(f"enter the number between 0 and {top_of_range}"))
    if(input_number == random_number):
        print("corret!")
        break
    else:
        if(input_number>random_number):
            print("you were higher!!")
        elif(input_number<random_number):
            print("you were higehr than the number!!")
        continue
print(f"you got it in - {guess}")
    

