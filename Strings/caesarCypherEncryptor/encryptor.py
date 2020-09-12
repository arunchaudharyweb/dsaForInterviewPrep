# O(n) time | O(n) space

def caesarCipherEncryptor(string, key):
	newString = list(string)
	for x in range(len(newString)):
		newString[x] = updateLetter(newString[x], key)
	return "".join(newString)

def updateLetter(newLetter, key):
	return chr((ord(newLetter) + key - 97) % 26 + 97)
for key in range(1, 27):   
	print(caesarCipherEncryptor("kzjupah", key), key)
	print(caesarCipherEncryptor("moznah", key), key)
	print(caesarCipherEncryptor("kq", key), key)
	print("")
# # O(n) time | O(n) space
# def caesarCipherEncryptor(string, key):
#     newLetters = []
# 	newKey = key % 26
# 	for letter in string:
# 		newLetters.append(getNewLetter(letter, newKey))
# 	return "".join(newLetters)

# def getNewLetter(letter, key):
# 	newLetterCode = ord(letter) + key
# 	return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 122)

