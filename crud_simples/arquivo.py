from os import system, path, remove, rename, name
from time import sleep
from colorama import Fore, Style

comandos = {
	"comando1": "ls",
	"comando2": "cd .."
}

def exibir_diretório():
	if name == "nt": system("dir")
	else: system("ls")


def criar_arquivo(nome):
	with open(nome, "w") as arquivo:
		sleep(2)
		print(f"{Fore.GREEN + nome + Fore.RESET} criado com sucesso")


def criar_multiplos_arquivos(nome, extensao,  quantidade):
		contador = 1
		while contador <= quantidade:
			nome_arquivo = nome + str(contador) + extensao
			with open(nome_arquivo, "w") as arquivo:
				contador += 1


def deletar_arquivo(nome_arquivo):
	if path.exists(nome_arquivo):
		remove(nome_arquivo)
	else:
		print("o arquivo não existe para ser deletado")


def deletar_multiplos(extensao):
		system(f"rm *{extensao}")


def renomear_arquivo(antigo_nome, novo_nome):
	if path.exists(antigo_nome):
		rename(antigo_nome, novo_nome)
		system(comandos.get("comando1"))
	
	else:
		print("o arquivo não existe ou não possui o nome informado")
		system(comandos.get("comando1"))


def renomear_multiplos(nomes, novos_nomes):
		contador = 0
		novos_nomes = list(novos_nomes)
		for x in nomes:
			if path.exists(x):
				rename(x, novos_nomes[contador])
				contador += 1
	

def ler_arquivo(nome):
	if path.exists(nome):
		system("cat " + nome)
	else:
		print("o arquivo não existe para ser lido")


def ler_arquivos(arquivos):
	for x in arquivos:
		system("cat " + x)


criar_multiplos_arquivos("a", ".py", 5)