# (02:53:59) 

# quiz game

# questions = (
#     "How many a's are in 'apple'?:",
#     "What comes after 'b' in 'ballons'?:",
#     "How many a's are in a 'word'?:"
# )

# options = (
#     ("A.34", "B.1", "C.2", "D.0"),
#     ("A.a", "B.b", "C.c", "D.d"),
#     ("A.34", "B.1", "C.2", "D.0")
# )

# answers = ("B", "A", "D")
# guesses = []
# score = 0

# for question_num in range(len(questions)):
#     print("-----------------------------------------")
#     print(questions[question_num])
#     for option in options[question_num]:
#         print(option)
    
#     guess = input("Enter your guess: ").upper()
#     guesses.append(guess)

#     if guess == answers[question_num]:
#         print("Correct!")
#         score += 1
#     else:
#         print(f"Wrong. The correct answer was {answers[question_num]}.")

# print("-----------------------------------------")
# print(f"You scored: {score}/3")