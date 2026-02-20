try:
    f = open("test.txt")
except NameError as e :
    print(e)
except Exception as e :
    print(e)
else:
    print(f.read())
    f.close
finally:
    print("program done nice to with you ")