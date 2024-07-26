# name = 'Alvin'
# number1 = '18'
# number2 = 22
# print(name[0].lower())
# print(name.lower())
# print(name + ' ' + number1)


num1 = float(input("Enter first number: "))
ops = input("What Operation you want to do? (+ - * /)")
num2 = float(input("Enter second number: "))
if ops == '+' or ops == 'plus':
    print("Output is: ", num1 + num2)
elif ops == '-':
    print("Output is: ", num1 - num2)
elif ops == '*':
    print("Output is: ", num1 * num2)
elif ops == '/':
    print("Output is: ", num1 / num2)
else:
    print("Invalid operation! Use only '+' '-' '*' or '/'")

color = input("Enter a Color: ")
plural_noun = input("Enter a Plural Noun: ")
celebrity = input("Enter a Celebrity: ")

print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)

