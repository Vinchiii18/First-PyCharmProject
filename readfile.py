# employee_file = open("index.html", "r")
# r - read
# a - append
# w - write/overwrite the entire file, can also be used to create new file

# OUTPUTS A LIST
# employee_list = employee_file.readlines()
# print(employee_list[0])

# CAN ALSO BE USED IN LOOPS
# for employee in employee_file.readlines():
#     print(employee)

# USE .write for 'w'
# employee_file.write("<p>This is HTML Paragraph</p>")

employee_file = open("employees.txt", "r")
print(employee_file.read())

employee_file.close()

