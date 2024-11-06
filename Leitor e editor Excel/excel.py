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
	
	def alterar_valor(self, planilha, row, column):
		alterar = input("deseja alterar ou inserir algum valor: ")
		if alterar == "" or alterar != "s":
			verificar_sistema()
		elif alterar != "":
			if planilha != "3":
				sheet = workbook[planilha]
				while row < 100:
					cell_name = sheet[column[0] + str(row)].value
					if cell_name == None:
						break
					else:
						print(f"{column + str(row)}:{cell_name}")
					row += 1
				celula = input("digite nome da célula que quer modificar: ")
				new_value = input(f"digite o novo valor da celula {celula}: ").upper()
				sheet[celula] = new_value
				workbook.save('registros.xlsx')

			else:
				sheet = workbook[planilha]
				while row < 100:
					cell_name = sheet[column[0] + str(row)].value
					cell_value = sheet[column[1] + str(row)].value
					if cell_name == None:
						break
					else:
						print(f"{cell_name}:{cell_value}")
				celula = input("digite o nome da célula que quer modificar: ")
				value = input(f"digite o novo valor da celula {celula}: ")
				sheet[celula] = value
				workbook.save('registros.xlsx')


	def exibir_planilha(self, planilha, row, column):
		if planilha != 3:
			sheet = workbook[planilha]
			while row < 100:
				#gambiarra feita aqui, arrume dps, feita pra rodar todas as planilhas
				#senão ou pega as planilhas 1,2 e 4 e não a 3 ou vice versa
				#tem haver com a 3 ter uma lista de parametros e as outras não
				#corrigi ai nathan do futuro
				cell = Fore.GREEN + column[0] + str(row) + Fore.RESET
				cell_value = sheet[column[0] + str(row)].value
				if cell_value == None:
					break
				else:
					print(f"{cell}: {cell_value}")
					row += 1
			self.alterar_valor(planilha, row, column)
				
		else:
			sheet = workbook[planilha]
			while row < 100:
				cell = Fore.GREEN + column[0] + str(row) + Fore.RESET
				cell_name = sheet[column[0] + str(row)].value
				cell_value = sheet[column[1] + str(row)].value
				if cell_value == None:
					break
				else:
					print(f"{cell}: {cell_name}: {cell_value}")
					row += 1
			self.alterar_valor(planilha, row, column)

	def chamar_planilha(self):
		choice = input("""
qual planilha quer abrir:
1- filmes
2- mangas
3- digital tamers
4- jogos
""" + "\n")
		match choice:
			case "1":
				self.exibir_planilha('FILMES', 2, 'a')

			case "2":
				self.exibir_planilha('MANGAS', 2, 'a')

			case "3":
				self.exibir_planilha("DIGITAL TAMERS", 10, ["c", "d"])

			case "4":
				self.exibir_planilha('JOGOS', 4, 'c')
			
			case _:
				verificar_sistema()

sasa = excel()
sasa.chamar_planilha()
