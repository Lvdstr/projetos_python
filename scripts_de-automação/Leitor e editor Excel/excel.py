from os import system, name
from colorama import Fore
from openpyxl import load_workbook


mensagem = f"""
qual planilha quer abrir:
1- {Fore.GREEN + "filmes" + Fore.RESET}
2- {Fore.GREEN + "mangas"+ Fore.RESET}
3- {Fore.GREEN + "digital tamers"+ Fore.RESET}
4- {Fore.GREEN + "jogos"+ Fore.RESET}
"""


try:
        workbook = load_workbook('/data/data/com.termux/files/home/scripts/exceu/registros.xlsx')
except:
        print("o arquivo foi removido patrão")


def alterar_valor(planilha):
	sheet = workbook[planilha]
	celula = input("digite nome da célula que quer modificar: ")
	if celula == "":
		system('clear')
	else:
		old_value = sheet[celula].value
		new_value = input(f"digite o novo valor da celula {celula}: ").upper()
		sasa = sheet[celula] = new_value
		workbook.save('/data/data/com.termux/files/home/scripts/exceu/registros.xlsx')
		print(f"valor antigo: {old_value}\nnovo valor: {new_value}")


def exibir_planilha(planilha, row, column):
        print(planilha)
        if planilha == "FILMES" or planilha == "JOGOS":
                sheet = workbook[planilha]
                while row < 100:
                        cell = Fore.GREEN + column[0] + str(row) + Fore.RESET
                        cell_value = sheet[column[0] + str(row)].value
                        if cell_value == None:
                                break
                        else:
                                print(f"{cell}: {cell_value}")
                                row += 1
                alterar_valor(planilha)

        elif planilha == "MANGAS":
                sheet = workbook[planilha]
                cell = Fore.GREEN + "  A:nomes       C:capitulos lidos" + Fore.RESET
                print(cell)
                while row < 100:
                        cell_value = sheet[column[0] + str(row)].value
                        cell_sasa = sheet[column[1] + str(row)].value
                        if cell_value == None:
                                break
                        else:
                                print(f"{row}: {cell_value}:  {cell_sasa}")
                                row += 1
                alterar_valor(planilha)

        elif planilha == "DIGITAL TAMERS":
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
                alterar_valor(planilha)


def chamar_planilha():
                choice = input(mensagem)
                match choice:
                        case "1":
                                exibir_planilha('FILMES', 2, 'a')
                        case "2":
                                exibir_planilha('MANGAS', 2, ['a', "c"])
                        case "3":
                                exibir_planilha("DIGITAL TAMERS", 10, ["c", "d"])
                        case "4":
                                exibir_planilha('JOGOS', 4, 'c')
                        case _:
                                pass
                                #verifiy_system()


chamar_planilha()