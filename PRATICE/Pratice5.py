# The Robust Calculator(functions,try except,map,split())

# Create a function calculate(num1, num2, operation) that performs addition, subtraction, multiplication, or division.
# The Twist: Wrap the user input in a while True loop. Use try/except to catch ValueError (if they type "abc" instead of a number) and ZeroDivisionError.
# Goal: The program should never crash, no matter what the user types


def calculate(num1,num2,operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        if num1>=num2:
            return num1-num2
        else:
            return num2-num1
    elif operator == "/":
        choice = int(input("enter the choice: (1. num1/num2 or 2. num2/num1)"))
        if choice == 1:
            return num1/num2 
        elif choice == 2:
            return num2/num1
        if choice!= 1 or choice!= 2:
            print("cant proceed enter only 1 or 2")
    elif operator == "*":
        return num1*num2
    else:
        print("can't proceed wrong operator only (+ , - , / , *) ")


while True:
    try:
        User_input = input("enter number 1 and number 2 seperated with a space or TYPE exit : ")
        if User_input == "exit" or User_input == "EXIT" or User_input == "Exit":
            break
        choice = input("enter the operator only + - * / : ")
        num1,operator,num2 = map(int, User_input.split())
        a  = calculate(num1,num2,choice)
        print(f"the answer is:{a}")
    except ValueError:
        print("only enter number")
    except ZeroDivisionError:
        print("number 2 can't be zero")
    except Exception as e:
        print(f"an unexpected error accoured - {e}")

    

    




