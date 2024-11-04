from openpyxl import load_workbook
from os import system, name
from colorama import Fore, Style


def verificar_sistema():
	if name == "nt":
		system("cls")
	else:
		system("clear")

try:
	workbook = load_workbook('registros.xlsx')
except:
	print("o arquivo foi removido patrão")

class excel():
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


	def exibir_planilha(self, planilha, row, itera, column):
		if planilha != 3:
			sheet = workbook[planilha]
			for x in range(itera):
				cell = Fore.GREEN + column + str(row) + Fore.RESET
				cell_value = sheet[column + str(row)].value
				print(f"{cell}: {cell_value}")
				row += 1

		else:
			sheet = workbook[planilha]
			for x in range(itera):
				cell = Fore.GREEN + column[0] + str(row) + Fore.RESET
				cell_name = sheet[column[0] + str(row)].value
				cell_value = sheet[column[1] + str(row)].value
				print(f"{cell}: {cell_name}: {cell_value}")
				row += 1

	def chamar_planilha(self):
		choice = int(input("""
qual planilha quer abrir:
1- filmes
2- mangas
3- digital tamers
4- jogos
"""))
		print("\n")
		
		match choice:
			case 1:
				self.exibir_planilha('FILMES', 2, 7, 'a')

			case 2:
				self.exibir_planilha('MANGAS', 2, 63, 'a')

			case 3:
				self.exibir_planilha("DIGITAL TAMERS", 10, 26, ["c", "d"])

			case 4:
				self.exibir_planilha('JOGOS', 4, 20, 'c')
		
		choice = input("\ndeseja editar alguma planilha: ").lower()
		if choice == "s":
			self.editar_planilha()
		else:
			verificar_sistema()
			print("chau então")

sasa = excel()
sasa.chamar_planilha()