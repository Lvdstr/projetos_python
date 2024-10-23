from colorama import Fore, Style
from tinydb import TinyDB, Query

database = TinyDB('respostas.json')

# def verificar_jogador(key, value):
#	return database.contains(consulta[key] == value)
#funcao para verificar registros no banco

resposta_certas = [
	'sim',
	'sim',
	'sim',
	'nao',
	'sim',
	'nao',
	'sim',
	'sim',
	'sim',
	'sim'
]

opcoes_resposta = [
	'sim',
	'nao'
]

perguntas = {
	'pergunta1': 'o selo amaldiçoado de Sasuke é o selo do céu: ',
	'pergunta2': 'a real identidade de pain é nagato: ',
	'pergunta3': 'sasuke ems é tao forte quanto itachi: ',
	'pergunta4': 'gogeta é mais forte que vegetto: ',
	'pergunta5': 'python é a linguagem mais superstimada de todas: ',
	'pergunta6': 'saitama é mais forte que goku: ',
	'pergunta7': 'garou é o melhor personagem de opm: ',
	'pergunta8': 'asta é mais forte que yuno: ',
	'pergunta9': 'yami é o capitão mais forte: '
}

respostas = []

def registrar_pontos(value):
	salvar_pontos = input("quer salvar teus pontos: ")
	if salvar_pontos == 's':
		nome_jogador = input("digite seu nome: ")
		database.insert({nome_jogador: value})

def exibir_respostas():
	contador = 0
	for x in range(len(opcoes_resposta)):
		print(opcoes_resposta[contador])
		contador += 1
	print(' ')
	res = input("resposta: ")
	respostas.append(res)
	print(' ')

def exibir_perguntas():
	iteracao = 1
	for x in range(len(perguntas)):
		print(perguntas.get('pergunta' + str(iteracao)))
		iteracao += 1
		exibir_respostas()

def exibirRespostasCorretas():
	pontos = 0
	print('respostas')
	for number, value in enumerate(respostas, 1):
		if value in resposta_certas:
			print(f'{number}: resposta correta: {Fore.GREEN + value + Fore.RESET}')
			pontos += 1
		else:
			print(f'{number}: resposta errada: {Fore.RED + value + Fore.RESET}')
	print(f'tu marcou {pontos} pontos')
	registrar_pontos(pontos)

def iniciar_quizz():
	print("bem vindo ao joguin de quizz")
	per = input('deseja jogar o quizz: ').lower()
	if per == 's':
		exibir_perguntas()
	else:
		print('chau')

iniciar_quizz()
exibirRespostasCorretas()