""" #hashing is ( can be f4567hdjduFG ) the purpose of hashing is to create a digital fingerprint """
""" #hashes are not reversible  """

import hashlib


# print(hashlib.algorithms_guaranteed)#print alll the available hshing algo available 


h = hashlib.new("SHA256") #OR h = hashlib.sha256()
# h.update(b"hello world!")
# print(h.digest())
# print(h.hexdigest())


password = "mypassword123"
h.update(password.encode())

password_hash = h.hexdigest()
print(password_hash)

user_input = "mypassword123"
h = hashlib.sha256()
h.update(user_input.encode())
input_hash = h.hexdigest()
print(input_hash)

print(password_hash == input_hash) 
