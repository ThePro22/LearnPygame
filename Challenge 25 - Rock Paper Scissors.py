#Challenge 25

import random, os
repeats = 0
while repeats < 3 or repeats > 10:
	try:
		repeats = int(input("Enter how many games you want to play between 3 and 10 "))
	except ValueError:
		repeats = 3
		print("You will play the game three times\n")

for x in range(repeats):
	options = ["Rock", "Paper", "Scissors"]
	computerChoice = options[random.randrange(0,2)]
	userChoice = input("Type 'Rock', 'Paper', or 'Scissors'").upper()

	if "ROCK" in userChoice:
		userChoice = options[0]
	elif "PAPER" in userChoice:
		userChoice = options[1]
	else:
		userChoice = options[2]

	if userChoice == options[0]:
		if computerChoice == options[0]:
			print("DRAW: Computer chose Rock as well")
		elif computerChoice == options[1]:
			print("COMPUTER WINS: Computer chose Paper, and Paper beats Rock")
		else:
			print("PLAYER WINS: Computer chose Scissors, and Rock beats Scissors")

	elif userChoice == options[1]:
		if computerChoice == options[1]:
			print("DRAW: Computer chose Paper as well")
		elif computerChoice == options[2]:
			print("COMPUTER WINS: Computer chose Scissors, and Scissors beats Paper")
		else:
			print("PLAYER WINS: Computer chose Rock, and Paper beats Rock")

	else:
		if computerChoice == options[2]:
			print("DRAW: Computer chose Scissors as well")
		elif computerChoice == options[0]:
			print("COMPUTER WINS: Computer chose Rock, and Rock beats Scissors")
		else:
			print("PLAYER WINS: Computer chose Paper, and Scissors beats Paper")
	print("\n"*2)

os.system("pause")