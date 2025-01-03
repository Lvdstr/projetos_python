from os import system, path, remove, rename, name
from time import sleep
from colorama import Fore, Style


comandos = {
	"comando1": "ls",
	"comando2": "cd .."
}


def limpar_terminal():
    match name:
        case "nt": system("cls")
        case _: system("clear")


def exibir_diretório():
	"""exibir todos os arquivos do diretório onde esta esse código"""
	if name == "nt": system("dir")
	else: system("ls")


def criar_arquivo(nome):
	"""
	recebe um nome formado por nomeDoArquivo + .extensãoDoArquivo,
	cria um arquivo com o formato write,
	atrasa o código em 2 segundos,
	exibe no console uma mensagem formatada em verde que o arquivo vai criar
	"""
	limpar_terminal()
	try:
		with open(nome, "w") as arquivo:
			sleep(2)
			print(f"{Fore.GREEN + nome + Fore.RESET} criado com sucesso")
	except FileNotFoundError:
		print("kkkkk")


def criar_multiplos_arquivos(nome, extensao,  quantidade):
		limpar_terminal()
		contador = 1
		while contador <= quantidade:
			nome_arquivo = nome + str(contador) + extensao
			with open(nome_arquivo, "w") as arquivo:
				contador += 1


def deletar_arquivo(nome_arquivo):
	limpar_terminal()
	if path.exists(nome_arquivo):
		remove(nome_arquivo)
	else:
		print("o arquivo não existe para ser deletado")


def deletar_multiplos(extensao):
		limpar_terminal()
		system(f"rm *{extensao}")


def renomear_arquivo(antigo_nome, novo_nome):
	limpar_terminal()
	if path.exists(antigo_nome):
		rename(antigo_nome, novo_nome)
		system(comandos.get("comando1"))
	
	else:
		print("o arquivo não existe ou não possui o nome informado")
		system(comandos.get("comando1"))


def renomear_multiplos(nomes, novos_nomes):
		limpar_terminal()
		contador = 0
		novos_nomes = list(novos_nomes)
		try:
			for x in nomes:
				if path.exists(x):
					rename(x, novos_nomes[contador])
					contador += 1
		except PermissionError as error:
			print("não a permissão para fazer modificação/ões")
	

def ler_arquivo(nome):
	limpar_terminal()
	if name == "nt":
		print("é windows mané")
	else:
		if path.exists(nome):
			system("cat " + nome)
		else:
			print("o arquivo não existe para ser lido")


def ler_arquivos(arquivos):
	limpar_terminal()
	if name == "nt":
		print("é windows mané")
	else:
		for x in arquivos:
			system("cat " + x)


renomear_arquivo("a.py", "matter.py")