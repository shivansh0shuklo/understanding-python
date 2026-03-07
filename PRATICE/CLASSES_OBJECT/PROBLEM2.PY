#Problem 3: The FileSecret Class (Data Protection)

class Filesecret():
    def __init__(self,filename,secret_key):
        self.filename = filename 
        self.secret_key = secret_key
    def is_authorized(self,key_attempt):
        return key_attempt == self.secret_key
    

file  = [Filesecret('one',45),Filesecret('two',50)]
key = int(input("enter the key: "))
# print(file[0].is_authorized(key))
for f in file:
    if (f.is_authorized(key)):
        print("access granted to file: {}".format(f.filename))
        break