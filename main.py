#	@Author: Nick Haynes
def is_isogram(string):
	for char in string:
		if string.count(char) == 1:
			print(char + " Doesn't repeat")

		else:
			print("The repeating letter is " + char)



is_isogram("Hello")