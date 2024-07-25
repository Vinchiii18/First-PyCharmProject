# name = 'Alvin'
# number1 = '18'
# number2 = 22
# print(name[0].lower())
# print(name.lower())
# print(name + ' ' + number1)


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
ops = input("What Operation you want to do?")

if ops == '+':
    result = num1 + num2
    print("Output is: ", result)
elif ops == '-':
    result = num1 - num2
    print("Output is: ", result)
elif ops == '*':
    result = num1 * num2
    print("Output is: ", result)
elif ops == '/':
    result = num1 / num2
    print("Output is: ", result)
else:
    print("Invalid operation! Use only '+' '-' '*' or '/'")

color = input("Enter a Color: ")
plural_noun = input("Enter a Plural Noun: ")
celebrity = input("Enter a Celebrity: ")

print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)

