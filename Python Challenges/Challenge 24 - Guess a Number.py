#Challenge 24
import random

guess = ""
guessCount = 0
print("I've thought of a number between 1 and 10. Try to guess it.")

randomNumber = random.randrange(1,10)

while guess != randomNumber:
	guess = int(input("Guess the number: "))
	if guess != randomNumber:
		print("You got it wrong")
		guessCount += 1

print("It took you", guessCount, "guesses to guess my number!")
input("Well done. Press ENTER to exit ")