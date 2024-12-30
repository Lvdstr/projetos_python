from random import randint
from tinydb import TinyDB, Query
from colorama import Fore, Back, Style
from faker import Faker

fake = Faker('pt_BR')
database = TinyDB('contas_registradas.json')
consulta = Query()


def gerar_dados():
	"""gera 3 valores: um nome, um cpf e um rg, retorna esses 3 valores pra serem usados como valores pra registro no banco"""
	nome = fake.name()
	cpf = fake.cpf()
	rg = fake.random_number(digits=9)
	return [nome, cpf, rg]


def verificar_registro(key, value):
	return database.contains(consulta[key] == value)
	"""verifica se um cadastro ja foi feito no banco de dados"""


def saldo(nome):
	"""verificar o saldo de um indivíduo, usando seu cpf como parametro de busca"""
	saldo = input("deseja verificar seu saldo: ")
	if saldo == 's':
		value = database.search(consulta.cpf == nome)
		print(value)


def registrarNoBanco(nome, cpf, rg, depositoInicial):
	"""obtém 4 valores, verifica se esses valores ja estão registrados, se nao estiverem registra no banco de dados"""
	registro = f'conta n:{str(randint(1, 10))}'
	informações_usuario = f"nome: {nome}\ncpf: {cpf}\nrg: {rg}\ndeposito inical: {depositoInicial}"

	if verificar_registro(registro, cpf):
		print(Fore.RED + "usuario ja registrado " + Fore.RESET)
	else:
		database.insert({registro: nome, 'cpf': cpf, 'rg': rg, 'saldo': depositoInicial})
		print(f"{informações_usuario}\n{Fore.GREEN + "usuario registrado com sucesso" + Fore.RESET}")

sasa = input("""oq quer fazer:
1. registrar usuário no banco
2. verificar conta
""")