import random

feet_in_mile = 5280
meters_in_kilometer = 1000
beatles = ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Star"]

# def get_file_ext(filename):
#     return filename[filename.index(".")+ 1:]

def get_file_ext(filename):
    if '.' in filename:
        return filename.rsplit('.', 1)[-1]
    return ''

# def roll_dice(num):
#     return random.randint(1, num)

def roll_dice(num):
    if num < 1:
        raise ValueError("Number of sides must be at least 1.")
    return random.randint(1, num)