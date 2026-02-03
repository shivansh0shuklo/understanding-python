# The Temperature Converter (Easy)(functions,try except)
# Write a function convert_to_celsius(fahrenheit) that performs the math.

def convert_to_celsius(fahrenheit):
    return ((fahrenheit-32)*0.55555555555555)


try:
    temp = float(input("eneter the temprature in fahrenheit: "))
    a = convert_to_celsius(temp)
except ValueError:
    print("only enter a decimal values!!")
finally:
    print(f"the temprature in celsius is - {a}")
