import csv, sys, re, random

choices = ["Rock","Scissors","Paper"]
user_score, sys_score = 0,0

print("Welcome to Rock, Paper, Scissors. The Game will be First to 3 points")
print('What would you like to play up to? You can exit at anytime by Typing Quit')
limit = input('> ').title()
print("playing to ",limit)
while True:

    print('Enter a Your Choice')
    user_input = input('> ').title()

    system_guess = random.choice(choices)

    if user_input == 'Quit':
        print('Thanks for playing :)')
        sys.exit()

    if user_input == "Rock" and system_guess == "Scissors":
        print("You Win!!")
        print("Computer chose Scissors")
        user_score += 1
    elif user_input == "Scissors" and system_guess == "Paper":
        print("You Win!!")
        print("Computer chose Paper")
        user_score += 1
    elif user_input == "Paper" and system_guess == "Rock":
        print("You Win!!")
        print("Computer chose Rock")
        user_score += 1
    elif user_input == system_guess:
        print("You Tied!!")
    else:
        print("You Lost")
        print("Computer chose ",system_guess)
        sys_score +=1
    
    print("Current Score --> Player: ", user_score, " System: ", sys_score)

    if user_score == int(limit):
        print("Well done, You beat the Computer!!")
        print("Final Score --> Player: ", user_score, " System: ", sys_score)
        sys.exit()
    elif sys_score == int(limit):
        print("Unlucky, you lost to a computer")
        print("Final Score --> Player: ", user_score, " System: ", sys_score)
        sys.exit()
