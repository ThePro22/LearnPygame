#Challenge 15

people = int(input("How many people are there? "))
bill = int(input("How much does the bill cost? £"))
tipPercentage = int(input("What percentage of the bill do you want to tip? "))

totalCost = bill + (bill / 100 * tipPercentage)

costPerPerson = totalCost / people

print("Each person has to pay £" + str(costPerPerson))