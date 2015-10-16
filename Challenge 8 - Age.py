#Challenge 8
name = input("What is your name? ")
age = float(input("How many years old are you? "))

daysAlive = age * 365
minutesAlive = daysAlive * (24*60)
secondsAlive = minutesAlive * 60

print("You have been alive for approximately", daysAlive, "days")
print("You have been alive for approximately", minutesAlive, "minutes")
print("You have been alive for approximately", secondsAlive, "seconds")