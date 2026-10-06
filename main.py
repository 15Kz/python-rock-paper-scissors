import random

choice = [
    "Rock",
    "Paper",
    "Scissor",
]

while True:
    randomBot = random.choice(choice)


    print("[1] Rock")
    print("[2] Paper")
    print("[3] Scissor")
    user = input("Enter choice: ")

    if user not in choice:
        print("Invalid Choice")
    elif user == randomBot:
        print("It's a tie!")
    elif (user == "Rock" and randomBot == "Scissor") or \
        (user == "Paper" and randomBot == "Rock") or \
        (user == "Scissor" and randomBot == "Paper"):
        print("You win!")
    else:
        print("You lose!")

