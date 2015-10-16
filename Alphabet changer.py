text = "http://www.pythonchallenge.com/pc/def/map.html"
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabetList = []

for letter in alphabet:
	alphabetList.append(letter)

for letter in text:
	if letter in alphabetList:
		value = (alphabetList.index(letter) + 2) % 26
		print(alphabetList[value], end='')
	elif letter == ' ':
		print(' ', end='')
