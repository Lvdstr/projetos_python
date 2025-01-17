from shutil import copy
from Lfile_auxiliar import *


def criar_arquivo(nome):
	"""
cria um arquivo usando o parâmetro nome
	"""
	limpar_terminal()
	try:
		with open(nome, "w") as arquivo:
			sleep(2)
			print(f"{Fore.GREEN + nome + Fore.RESET} criado com sucesso")
	except FileNotFoundError:
		print("kkkkk")


def criar_multiplos_arquivos(nome, extensao,  quantidade):
	"""
cria determinado número de arquivos usando uma combinação de nome + extensão
	"""
	limpar_terminal()
	contador = 1
	while contador <= quantidade:
		nome_arquivo = nome + str(contador) + extensao
		with open(nome_arquivo, "w") as arquivo:
			contador += 1


def deletar_arquivo(nome_arquivo):
	"""
verifica se um arquivo existe, se existir apaga ele
	"""
	try:
		limpar_terminal()
		if path.exists(nome_arquivo):
			remove(nome_arquivo)
		else:
			print("o arquivo não existe para ser deletado")
	except Exception as error:
		print(error)


def deletar_multiplos(extensao):
	"""
deleta multiplos arquivos com uma mesma extensão
	"""
	try:
		limpar_terminal()
		system(f"rm *{extensao}")
	except Exception as error:
		print(error)


def renomear_arquivo(antigo_nome, novo_nome):
	"""
verifica se um arquivo existe, se sim renomeia ele
	"""
	try:
		limpar_terminal()
		if path.exists(antigo_nome):
			rename(antigo_nome, novo_nome)
			exibir_diretório()	
		else:
			print("o arquivo não existe ou não possui o nome informado")
			exibir_diretório()
	except Exception as error:
		print(error)


def renomear_multiplos(nomes, novos_nomes):
	"""
percorre a lista de nomes, verificando se cada arquivo existe, se sim renomeia ele
usando um item de index correpondente da lista de novos nomes
	"""
	limpar_terminal()
	contador = 0
	novos_nomes = list(novos_nomes)
	try:
		for x in nomes:
			if path.exists(x):
				rename(x, novos_nomes[contador])
				contador += 1
			else:
				print("arquivo não encontrado ou inexistente")
	except PermissionError as error:
		print("não a permissão para fazer modificação/ões")
	

def ler_arquivo(nome):
	"""
verifica se um arquivo existe, se existe exibe o conteúdo na tela
	"""
	try:
		limpar_terminal()
		if name == "nt":
			print("é windows mané")
		else:
			if path.exists(nome):
				system("cat " + nome)
			else:
				print("o arquivo não existe para ser lido bro")
	except Exception as error:
		print(error)


def ler_arquivos(arquivos):
	"""
percorre uma lista de arquivos, verifica se o item atual existe
exibe o conteúdo na tela
	"""
	try:
		limpar_terminal()
		if name == "nt":
			print("é windows mané")
		else:
			for x in arquivos:
				if path.exists(x):
					system("cat " + x)
				else:
					print("o arquivo não existe para ser lido bro")
	except Exception as error:
		print(error)


def copiar(arquivo, arquivo_copia):
	try:
		if path.exists(arquivo):
			copy(arquivo, arquivo_copia)
			print(f"arquivo: {arquivo} copiado com sucesso")
		else:
			print("o arquivo não existe para ser copiado bro")
	except Exception as error:
		print(f"erro encontrado: {error}")


def copiar_arquivos(arquivos, cópias):
	for x in [arquivos, cópias]:
		a = list_verify(x)
		if a ==  True:
			limpar_terminal()
			contador = 0
			novos_arquivos = list(cópias)
			try:
				for x in arquivos:
					if path.exists(x):
						copy(x, cópias[contador])
						contador += 1
			except Exception as error:
				print(error)
		else:
			print("perdeu, perdeu fudeu")