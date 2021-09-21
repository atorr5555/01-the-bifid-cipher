import fileinput
import string

# Funcion que llena la tabla usando la llave
# y el alfabeto restante
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

# Funcion que busca un caracter en la tabla
# y devuelve su indice
def find_char(char):
	if char == 'J':
		raise Exception('J no soportada')
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
	# Crea alfabeto sin la J
	alphabet = list(string.ascii_uppercase.replace('J',''))
	# Quita del alfabeto los caracteres que estan en la llave
	for char in KEY:
		alphabet.remove(char)
	count = 0
	# Recibe la entrada
	for line in fileinput.input():
		if count == 0:
			action = line
			count += 1
			continue
		if count > 1:
			break
		phrase = line
	phrase = phrase.replace(' ', '')
	phrase = phrase.replace('\n', '')
	action = action.replace('\n', '')

	# Genera y llena la tabla
	table = [ [ 'A' for i in range(5) ]  for i in range(5) ]
	fill_table()
	
	# Encuentra los indices de los caracteres
	aux = []
	for char in phrase:
		aux.append(find_char(char))

	# Revisa cual es la accion a realizar
	if action == 'ENCRYPT':
		# Concatena los elementos de los indices
		string_nums = ''
		for x in aux:
			string_nums += str(x[0])

		for x in aux:
			string_nums += str(x[1])

		# Genera nuevos indices agrupando en pares
		# los indices concatenados
		nuevas_coords = []
		for i in range(0, len(string_nums), 2):
			nuevas_coords.append((int(string_nums[i]), int(string_nums[i+1])))

		# Encuentra las letras acordes a los nuevos indices generados
		cifrado=''
		for x in nuevas_coords:
			cifrado += table[x[0]][x[1]]
		print(cifrado)
	else:
		# Concatena los elementos de los indices
		string_nums = ''
		for x in aux:
			string_nums += str(x[0])
			string_nums += str(x[1])
		
		# Divide la cadena con indices en dos partes
		break_point = int(len(string_nums) / 2)
		parte1 = string_nums[:break_point]
		parte2 = string_nums[break_point:]

		# Genera nuevos indices usando las dos partes generadas
		coord_origen = [(int(parte1[i]), int(parte2[i])) for i in range(break_point)]

		# Usando los nuevos indices encuentra la frase original
		original = ''
		for x in coord_origen:
			original += table[x[0]][x[1]]
		print(original)
