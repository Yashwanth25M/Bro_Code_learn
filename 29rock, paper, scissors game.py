# # (03:32:37)

# # rock, paper, scissors game

# import random

# t = ("rock", "paper", "scissor")
# print('Welcome to "rock", "paper", "scissor" game')
# print("You are provided 3 rounds")

# c_score = 0
# p_score = 0

# for i in range(1, 4):
#     print(f"\nRound {i}")
#     computer = random.choice(t)
#     player = input("Enter your choice ('rock', 'paper', 'scissor'): ").lower()
#     print(f"Player choice: {player}\nComputer choice: {computer}")

#     if player not in t:
#         print("Invalid input. Computer gets the point.")
#         c_score += 1
#         continue

#     if player == computer:
#         print("OH TIE!!")
#         c_score += 1
#         p_score += 1
#     else:
#         if player == "rock":
#             if computer == "paper":
#                 print("Computer won this round!")
#                 c_score += 1
#             else:
#                 print("You won this round!")
#                 p_score += 1
#         elif player == "paper":
#             if computer == "scissor":
#                 print("Computer won this round!")
#                 c_score += 1
#             else:
#                 print("You won this round!")
#                 p_score += 1
#         elif player == "scissor":
#             if computer == "rock":
#                 print("Computer won this round!")
#                 c_score += 1
#             else:
#                 print("You won this round!")
#                 p_score += 1

# print("\nFinal Scores:")
# print(f"Player: {p_score}")
# print(f"Computer: {c_score}")

# if p_score > c_score:
#     print("Congratulations! You won the game!")
# elif p_score < c_score:
#     print("Computer won the game! Better luck next time.")
# else:
#     print("It's a tie game!")