# i = 1
# while i <= 10:
#     print(i)
#     i += 1
#
# print("Done with loop!")

# Basic Guessing Game

secret_word = "giraffe"
guess = ""
guess_limit = 10

print("You can try and guess up to 10 times only!")
while guess_limit >= 0:
    guess = input("Enter a word: ")
    guess_limit -= 1

    if guess == secret_word:
        print("You got the secret word correctly!")
        break
    elif guess_limit == 0:
        print("Game Over! Limit Reached!")
        break
    else:
        print("Word is incorrect! You still have "
            + str(guess_limit) + " "
            + ("try" if guess_limit == 1 else "tries") + " left!")

# YOUTUBE SOLUTION
# secret_word = "giraffe"
# guess = ""
# guess_count = 0
# guess_limit = 10
# out_of_guesses = False
#
# while guess != secret_word and not out_of_guesses:
#     if guess_count < guess_limit:
#         guess = input("Enter a word: ")
#         guess_count += 1
#     else:
#         out_of_guesses = True
#
# if out_of_guesses:
#     print("Game Over! Limit Reached!")
# else:
#     print("You got the secret word correctly!")
    
# ChatGPT solution
# secret_word = "giraffe"
# guess = ""
# guess_limit = 10
#
# print("You can try and guess up to 10 times only!")
# while guess_limit > 0:
#     guess = input("Enter a word: ")
#     guess_limit -= 1
#
#     if guess == secret_word:
#         print("You got the secret word correctly!")
#         break
#     elif guess_limit == 0:
#         print("Game Over! Limit Reached!")
#     else:
#         print(f"Word is incorrect! You still have {guess_limit} {'try' if guess_limit == 1 else 'tries'} left!")
