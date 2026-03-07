#Problem 1: The "Secure Vault" (Classes & File I/O)

class vault:
    def __init__(self,file_name):
        self.file_name = file_name
    def add_secret(self,secret):
            try:
                with open(self.file_name,'a') as f:
                    for individual_secrets in secret: 
                        f.write(individual_secrets+"\n")
            except PermissionError:
                print("permisson denied!!")
    def read_secrets(self):
        try:
            with open(self.file_name,'r') as f:
                for lines in f:
                    yield lines.strip()
        except FileNotFoundError:
            print("file not found")
        except IOError:
            print("a i/o error occured !!")

file = vault("test.txt")
secrets = ['hello','this is new','this has never happend before']
file.add_secret(secrets)
for i in file.read_secrets():
    print(i+" \t")