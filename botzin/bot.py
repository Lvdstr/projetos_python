from tinydb import TinyDB, Query
from os import system
from colorama import Fore, Back, Style
import bibliotecas

database = TinyDB('nome.json')

def definir_nome():
	nome = input("digite o nome do bot: ")
	database.insert({"nomeDoBot": nome})
	system('python reinicio.py')

def apresentação(nome=''):
	if nome == '':
		print("Olá, este é um bot em desenvolvimento, defina um nome para que possamos continuar")
		definir_nome()
	else:
		print(f"Olá, aqui é seu bot {nome}")
		funcões_do_bot()

def verificar_nome():
	chave = 'nomeDoBot'
	value = database.all()
	if len(value) != 0:
		for x in value:
			if chave in x:
				sasa = Fore.GREEN + x[chave] + Fore.RESET
				apresentação(sasa)
	else:
		apresentação()

def funcões_do_bot():
	escolha = input("""
escolha uma das opcoes de ações possiveis de serem realizadas:
1-verificar as planilhas excel
2-mudar pra alguma pasta da codigos
""")

	match escolha:
		case '1':
			system('excel')
		case _:
			system('clear')
			print("bele, até a próxima")

verificar_nome()