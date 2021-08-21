s = input("Enter the String: ")
char_count = {}

for i in s:
	if i in char_count:
		char_count[i] += 1
	else:
		char_count[i] = 1

print ("Count of all characters: "+ str(char_count))