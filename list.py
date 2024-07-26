array = ['alvin', 'dave', 'rene', 'mina', 'tin']

# Loop through each element in the array and capitalize the first letter
for i in range(len(array)):
    array[i] = array[i].capitalize()

print(array)


# Create a dictionary in Python
person = {
    'name': 'Alvin',
    'age': 35,
    'job': 'Web Dev'
}

# Accessing dictionary values
print(person['name'])  # Output: Alvin
print(person['age'])   # Output: 35
print(person['job'])   # Output: Web Dev

# Adding a new key-value pair
person['city'] = 'New York'

# Updating a value
person['age'] = 36

# Printing the updated dictionary
print(person)
