#Challenge 18
happiness = int(input("On a scale of 1 to 10, 1 being sad, 10 being happy, rate your current mood: "))
if happiness > 0 and happiness <= 3:
	print("I hope you feel better soon :)")
elif happiness > 0 and happiness <= 7:
	print("Cheer up!")
elif happiness > 0 and happiness <= 10:
	print("Great! Nice to see somebody so happy")
	