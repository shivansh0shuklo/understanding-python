# The Secure Login (Medium)(functions,split(),try except)
# # Create a program that mimics a simple login system using a function login(username, password).

def login(username,password):
    correct_user = "Afermeth"
    correct_pass = "hello123#"
    if username == correct_user and  password == correct_pass:
        return True
    else:
        return False
    
print("welcome to the program!!")
counter = 0
for i in range (0,3,1):
    user = input("enter the username ")
    password = input("enter the password ")
    try:
        if login(user,password):
            print("logined.....")
            break
        else:
            counter+=1
            if counter<3:
                print(f"WRONG CRED {3-counter} attempts left")
            else:
                raise Exception("to many failed attempts")
    except Exception as e:
        print(f"Aleart!! {e}")
        print("account locked!")
        break
