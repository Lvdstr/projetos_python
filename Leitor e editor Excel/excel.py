from openpyxl import load_workbook
from os import system

try:
	# abrir o arquivo
	workbook = load_workbook('registros.xlsx')
except:
	print("o arquivo foi removido patrão")

class excel():
	"""
	docstrings here
	"""
	def __init__(self):
		pass

	def alterar_valor(self, planilha, row, itera, column):
		if planilha != "3":
			sheet = workbook[planilha]
			for x in range(itera):
				cell_name = sheet[column + str(row)].value
				print(f"{column + str(row)}:{cell_name}")
				row += 1
			celula = input("digite nome da célula que quer modificar: ")
			new_value = input(f"digite o novo valor da celula {celula}: ").upper()
			sheet[celula] = new_value
			workbook.save('registros.xlsx')

		else:
			sheet = workbook[planilha]
			for x in range(itera):
				cell_name = sheet[column[0] + str(row)].value
				cell_value = sheet[column[1] + str(row)].value
				print(f"{cell_name}:{cell_value}")
			edit = input("digite o nome da célula que quer modificar: ")
			value = input(f"digite o novo valor da celula {edit}: ")
			sheet[edit] = value
			workbook.save('registros.xlsx')

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
				self.alterar_valor("FILMES", 2, 7, "a")

			case "2":
				self.alterar_valor("MANGAS", 2, 63, "a")

			case "3":
				self.alterar_valor("DIGITAL TAMERS", 10, 26, ["c", "d"])	

			case "4":
				self.alterar_valor("JOGOS", 4, 20, "c")

	def ler_planilha(self, planilha, row, itera, column):
		if planilha != "3":
			sheet = workbook[planilha]
			print("\n")
			for x in range(itera):
				cell_name = sheet[column + str(row)].value
				print(cell_name)
				row += 1
		else:
			sheet = workbook[planilha]
			for x in range(itera):
				cell_name = sheet[column[0] + str(row)].value
				cell_value = sheet[column[1] + str(row)].value
				print(f"{cell_name}:{cell_value}")
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
				self.ler_planilha('FILMES', 2, 7, 'a')

			case "2":
				self.ler_planilha('MANGAS', 2, 63, 'a')

			case "3":
				self.ler_planilha("DIGITAL TAMERS", 10, 26, ["c", "d"])

			case "4":
				self.ler_planilha('JOGOS', 4, 20, 'c')
		
		other = input("\ndeseja editar alguma planilha: ").lower()
		if other == "s":
			self.editar_planilha()
		else:
			system("clear")
			print("chau então")

sasa = excel()
sasa.abrir_planilha()