#Challenge 16

import random

answerOne = "Absolutely!"
answerTwo = "No way Pedro!"
answerThree = "Go for it tiger."
answerFour = "Sorry. I can't answer that..."
answerFive = "Follow your heart"

print("Welcome to Magic 8 Ball game \n Use it to answer your questions")

question = input("Ask me for any advice and I’ll help you out. Type in your question and then press Enter for an answer: ")

print("shaking... \n" * 4)

choice = random.randint(1,3)

if choice == 1:
	answer = answerOne
elif choice == 2:
	answer = answerTwo
elif choice == 3:
	answer = answerThree
elif choice == 4:
	answer = answerFour
else:
	answer = answerFive


print(answer)