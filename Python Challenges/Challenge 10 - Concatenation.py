#Challenge 10

wishList = []

print("You will be asked three times for a different item you want for christmas")

for x in range(3):
	gift = input(str(x + 1) + ") Name something you want for christmas ")
	wishList.append(gift)

giftList = wishList[0] + " " + wishList[1] + " " + wishList[2]

print(giftList)
