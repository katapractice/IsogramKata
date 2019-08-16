#	@Author: Nick Haynes
def is_isogram(string):
	string = string.lower()
	for char in string:
		if string.count(char) == 1:
			print(char + " Doesn't repeat")

		else:
			print("The repeating letter is " + char)
			return False

	return True


print(is_isogram("moose"))