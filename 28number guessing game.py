# (03:24:16)

# number guessing game

# import random

# answer = random.randint(1,100)
# guesses = 1

# print("Lets play a guessing a number game!!")
# print("Select a number between 1 and 100")
# print(answer)
# while True:
#     inn = input("Enter your guess:")
#     if inn == "done":
#         print("You lose\nTotal number of gueese:",guesses)
#         break
#     else:
#         inn = int(inn)
#         if(inn == answer):
#             print(f"You guessed it correctly \nWith total guesses of {guesses} ")
#             break
#         elif(inn > answer):
#             print("Thinked of lower numbers")
#             guesses += 1
#         elif(inn < answer):
#             print("Thinked of Higher numbers")
#             guesses += 1