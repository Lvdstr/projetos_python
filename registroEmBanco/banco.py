from random import randint, randrange, choice, shuffle, sample
from tinydb import TinyDB, Query
from colorama import Fore, Back, Style
from faker import Faker

fake = Faker('pt_BR')
database = TinyDB('contas_registradas.json')
consulta = Query()


def gerar_dados():
	"""
	gera 3 valores: um nome, um cpf e um rg
	retorna esses 3 valores pra serem usados como valores pra registro no banco
	"""
	nome = fake.name()
	cpf = fake.cpf()
	rg = fake.random_number(digits=9)
	return [nome, cpf, rg]

def verificar_registro(key, value):
	return database.contains(consulta[key] == value)
	"""
	verifica se um cadastro ja foi feito no banco de dados
	"""

def saldo(cpf):
	"""
	verificar o saldo de um indivíduo, usando seu cpf como parametro de busca
	"""
	saldo = input("deseja verificar seu saldo: ")
	if saldo == 's':
		#database.update({'saldo': 9180}, consulta.cpf == cpf)
		#value = database.search(consulta.cpf == cpf)

def registrarNoBanco(nome, cpf, rg, depositoInicial):
	"""
	obtém 4 valores, verifica se esses valores ja estão registrados, se nao estiverem registra no banco de dados
	
	"""
	registro = f'conta n:{str(randint(1, 10))}'
	if verificar_registro(registro, nome):
		print(Fore.RED + "usuario ja registrado " + Fore.RESET)
	else:
		database.insert({registro: nome, 'cpf': cpf, 'rg': rg, 'saldo': depositoInicial})
		print(Fore.GREEN + "usuario registrado com sucesso" + Fore.RESET)

#dados = gerar_dados()
#registrarNoBanco(dados[0], dados[1], dados[2], 10)
#result = database.search(consulta.cpf ==)
#print(result)
saldo("297.351.486-09")