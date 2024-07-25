def say_hi(name, age):
    print("Hello " + name + "! You are " + str(age) + " years old!")


# say_hi("Alvin", 32)
# say_hi("Mina", 30)

def add(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise TypeError("Values you entered are not numbers. Please enter numbers only!")
    else:
        print("Output:", num1 + num2)


# Test the function with valid inputs
add(5, 5)

# Test the function with invalid inputs
try:
    add(5, 'hehe')
except TypeError as e:
    print(e)


def cube(num):
    return num*num*num


print(cube(2))
