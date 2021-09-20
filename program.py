import fileinput
import string

def fill_table():
	i=0
	j=0
	for char in KEY:
		table[i][j] = char
		j = (j+1) % 5
		if j == 0:
			i = (i+1) % 5
	index=0
	table[i][j] = alphabet[index]
	while i != 4 or j != 4:
		j = (j+1) % 5
		if j == 0:
			i = (i+1) % 5
		index = index + 1
		table[i][j] = alphabet[index]

def find_char(char):
	if char == 'J':
		return (-1, -1)
	i=0
	j=0
	for i in range(5):
		for j in range(5):
			if table[i][j] == char:
				return (i, j)
	

if __name__ == "__main__":
	KEY='ENCRYPT'
	action=''
	phrase=''
	alphabet = list(string.ascii_uppercase.replace('J',''))
	for char in KEY:
		alphabet.remove(char)
	count = 0
	for line in fileinput.input():
		if count == 0:
			action = line
			count += 1
			continue
		if count > 1:
			break
		phrase = line
	table = [ [ 'A' for i in range(5) ]  for i in range(5) ]
	fill_table()
	phrase = phrase.replace(' ', '')
	phrase = phrase.replace('\n', '')
	action = action.replace('\n', '')
	
	aux = []
	for char in phrase:
		aux.append(find_char(char))
	if action == 'ENCRYPT':
		string_nums = ''
		for x in aux:
			string_nums += str(x[0])

		for x in aux:
			string_nums += str(x[1])

		nuevas_coords = []
		for i in range(0, len(string_nums), 2):
			nuevas_coords.append((int(string_nums[i]), int(string_nums[i+1])))

		cifrado=''
		for x in nuevas_coords:
			cifrado += table[x[0]][x[1]]
		print(cifrado)
	else:
		string_nums = ''
		for x in aux:
			string_nums += str(x[0])
			string_nums += str(x[1])
		
		break_point = int(len(string_nums) / 2)
		parte1 = string_nums[:break_point]
		parte2 = string_nums[break_point:]

		coord_origen = [(int(parte1[i]), int(parte2[i])) for i in range(break_point)]

		original = ''
		for x in coord_origen:
			original += table[x[0]][x[1]]
		print(original)
