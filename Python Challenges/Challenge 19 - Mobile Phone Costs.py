#Challenge 19
pictures = float(input("How many pictures do you send every month? "))
texts = float(input("How many texts do you send every month? "))
data = float(input("How many MB of data do you use every month? "))

picturesCost = pictures * 0.35
textsCost = texts * 0.1
dataCost = data // 500 * 2.5

totalCost = picturesCost + textsCost + dataCost

print("You would spend £"+ str(totalCost), "every month on your phone")
if totalCost >= 10:
	print("You would save money if you were on a contract...")