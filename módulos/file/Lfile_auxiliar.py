from os import system, path, remove, rename, name
from time import sleep
from shutil import copy 
from colorama import Fore, Style


def limpar_terminal():
	"""
verifica qual é o sistema operacional e dependendo de qual é usa o comando
correspondente para limpar a tela do terminal 
	"""
	match name:
		case "nt": system("cls")
		case _: system("clear")


def exibir_diretório():
	"""
verifica qual é o sistema operacional e dependendo de qual é usa o comando
correspondente para exibir todos os arquivos do diretório atual
	"""
	if name == "nt": system("dir")
	else: system("ls")


def list_verify(value):
	if type(value) == list: 
		print("sim")
	else:
		return False