# for letter in "Giraffe Academy":
#     print(letter + 'A')

# friends = ['Alvin', 'Rene', "Dave", "Mina", "Arya"]
# for friend in friends:
#     print(friend)

# for index in range(10):
#     print(index) # will print 0 - 9 only, remember it started in index 0

# for index in range(3, 10):
#     print(index) # will print 3 - 9 only, remember it started in index 0

# friends = ['Alvin', 'Rene', "Dave", "Mina", "Arya"]
# for index in range(len(friends)):
#     print(friends[index])

# for index in range(5):
#     if index == 0:
#         print("First Iteration!")
#     else:
#         print("Not First!")

# def raise_to_power(base_num, pow_num):
#     result = 1
#     for index in range(pow_num):
#         result = result * base_num
#     return result
#
# print(raise_to_power(4,2))

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for row in number_grid:
    for col in row:
        print(col)