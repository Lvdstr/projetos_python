from random import choice, randint
from tinydb import TinyDB, Query
from colorama import Fore, Style

User = Query()
db = TinyDB('historico.json')
rand = randint(1, 1000)

def item_exists(key, value):
    return db.contains(User[key] == value)

def abrir_arquivo():
	try:
		abrir_arquivo = open("pokemons.txt", "r")
		lista_pokemons = abrir_arquivo.readlines()
		return lista_pokemons
	except:
		print("não foi possivel abrir o arquivo")
	finally:
		abrir_arquivo.close()


def registrarNoBanco(values):
	for x in values:
		if item_exists("pokemon_sorteado", x):
				print(Fore.RED + x)
		else:
			db.insert({"pokemon_sorteado": x})
			print(Fore.GREEN + x)

	
def sortear_pokemons(quanti_pokes):
	itens_sorteados = []
	arquivo_nomes = abrir_arquivo()
	for x in range(quanti_pokes):
		pokemon_sorteado = choice(arquivo_nomes)
		itens_sorteados.append(pokemon_sorteado)
	registrarNoBanco(itens_sorteados)
		
sortear_pokemons(6)