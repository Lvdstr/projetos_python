from openpyxl import load_workbook

try:
	# abrir o arquivo
	workbook = load_workbook('/data/data/com.termux/files/home/storage/shared/documents/excel/registros.xlsx')
except:
	print("o arquivo foi removido patrão")

class excel():
	"""
	docstrings here
	"""
	def __init__(self):
		pass

	def shinshin(self, planilha, row, itera, column):
		sheet = workbook[planilha]
		row = row
		for x in range(itera):
			cell_name = sheet[column + str(row)].value
			print(f"{column + str(row)} :{cell_name}")
			row += 1
		celula = input("digite nome da célula que quer modificar: ")
		new_value = input("digite o novo valor: ").upper()
		sheet[celula] = new_value
		workbook.save('/data/data/com.termux/files/home/storage/shared/documents/excel/registros.xlsx')

	def editar_planilha(self):
		choice = input("""
qual planilha quer editar:
1- filmes
2- mangas
3- digital tamers
4- jogos\n
""")
	
		match choice:
			case "1":
				self.shinshin("FILMES", 2, 7, "a")
			case "2":
				self.shinshin("MANGAS", 2, 63, "a")
			case "3":			
				# Selecionar a planilha pelo nome
				sheet = workbook['DIGITAL TAMERS']
				
				# Ler o conteúdo de uma célula específica (por exemplo, A1)
				number = 10
				for x in range(26):
					number += 1
					# concatena o nome da coluna que é uma letra com o numero da variavel que é aumentado toda vez pela iteração fo for
					cell_name = sheet['c' + str(number)].value
					cell_value = sheet['d' + str(number)].value
					print(f"{cell_name}:{cell_value}")
				edit = input("digite a célula que quer modificar: ")
				value = input("digite o valor: ")
				sheet[edit] = value
				workbook.save('/data/data/com.termux/files/home/storage/shared/documents/excel/registros.xlsx')
			case "4":
				self.shinshin("JOGOS", 4, 20, "c")

	def sasa(self, planilha, row, itera, column):
		sheet = workbook[planilha]
		row = row
		for x in range(itera):
			cell_name = sheet[column + str(row)].value
			print(cell_name)
			row += 1

	def abrir_planilha(self):
		choice = input("""
qual planilha quer abrir:
1- filmes
2- mangas
3- digital tamers
4- jogos
""")
		
		match choice:
			case "1":
				self.sasa('FILMES', 2, 9, 'a')
			case "2":
				self.sasa('MANGAS', 2, 63, 'a')
			case "3":
				# Selecionar a planilha pelo nome
				sheet = workbook['DIGITAL TAMERS']
				
				# Ler o conteúdo de uma célula específica (por exemplo, A1)
				number = 10
				for x in range(26):
					number += 1
					# concatena o nome da coluna que é uma letra com o numero da variavel que é aumentado toda vez pela iteração fo for
					cell_name = sheet['c' + str(number)].value
					cell_value = sheet['d' + str(number)].value
					print(f"{cell_name}:{cell_value}")
			case "4":
				self.sasa('JOGOS', 4, 20, 'c')
		
		other = input("\ndeseja editar alguma planilha: ").lower()
		if other == "s":
			self.editar_planilha()
		else:
			print("chau então")

sasa = excel()
sasa.abrir_planilha()