import random

print("Rock Paper Scissors")
print("1=Rock  2=Paper  3=Scissors")

user = int(input("Enter choice: "))
computer = random.randint(1, 3)

names = ["", "Rock", "Paper", "Scissors"]

print("User:", names[user])
print("Computer:", names[computer])

if user == computer:
    print("Draw")

elif (user == 1 and computer == 3) or \
     (user == 2 and computer == 1) or \
     (user == 3 and computer == 2):
    print("User Wins")

else:
    print("Computer Wins")
