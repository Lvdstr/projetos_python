from os import system, name
from time import sleep
from colorama import Fore
from openpyxl import load_workbook


def limpar_terminal():
    match name:
        case "nt": system("cls")
        case _: system("clear")


try:
        workbook = load_workbook('registros.xlsx')

        def verficaçõesNosValores(value):
                if value[0] > value[1]:
                        print(f"erro o primeiro valor é maior que o segundo\n{value[0]}\n{value[1]}\nnão haverá mudanças na planilha")
                        return False
                else:
                        return True


        def alterar_valor(planilha):
                sheet = workbook[planilha]
                celula = input("digite nome da célula que quer modificar: ")
                if celula != "":
                        old_value = sheet[celula].value
                        value = input(f"digite o novo valor da celula {celula}: ").upper()
                        new_value = int(value)
                        verificar = verficaçõesNosValores([old_value, new_value])
                        match verificar:
                                case True:
                                        sasa = sheet[celula] = new_value
                                        workbook.save('registros.xlsx')
                                        valores([old_value, new_value, planilha])
                                case _:
                                        return
                else:
                        limpar_terminal()


        def valores(values):
                print(f"valor antigo: {values[0]}\nnovo valor: {values[1]}")
                repeat = input("deseja repetir a planilha: ")
                if repeat == "s":
                        alterar_valor(values[2])
                else:
                        limpar_terminal()


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
                        limpar_terminal()
                        choice = input(f"""
qual planilha quer abrir:
1- {Fore.GREEN + "filmes" + Fore.RESET}
2- {Fore.GREEN + "mangas"+ Fore.RESET}
3- {Fore.GREEN + "digital tamers"+ Fore.RESET}
4- {Fore.GREEN + "jogos"+ Fore.RESET}
""")
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
                                        limpar_terminal()


        chamar_planilha()
        #system("python3 /data/data/com.termux/files/home/scripts/python/corrigir_caps.py")
except:
        print("o arquivo foi removido patrão")