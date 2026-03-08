##USING OS MODULE 
import os

#1. The "Path Validator" (Basics)

class fileguard:
    def __init__(self,folder_part):
        if(os.path.exists(folder_part)):
            if(os.path.isdir(folder_part)):
                print("all ok!!")
            else:
                print("it is not a folder ") 
        else:
            print("does not exists")

