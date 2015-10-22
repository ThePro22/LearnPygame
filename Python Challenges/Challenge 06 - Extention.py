#Challenge 6 - Extention
week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
totalMoney = float(input("How much money did you have at the start of the week? £"))
for day in range(5):
	cost = float(input("How much money did you spend on school dinner on " + week[day] +"? £"))
	totalMoney = totalMoney - cost

if totalMoney < 0:
	totalMoney = -totalMoney
	print("\nYou do not have sufficient funds. You need £" + str(totalMoney), "more")
else:
	print("\nYou have £" + str(totalMoney))