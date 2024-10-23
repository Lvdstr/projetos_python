from random import randint

lista = []

def number_generation(quanti, opcao):
	match opcao:
		case '1':
			for x in range(quanti):
				print(randint(1, 1000))
		
		case '2':
			while len(lista) < quanti:
				number = randint(1, 1000)
				if number % 2 == 0:
					lista.append(number)
				
			for contador, x in enumerate(lista, 1):
				print(f"{contador}: {x}")
		
		case '3':
			while len(lista) < quanti:
				number = randint(1, 1000)
				if number % 2 != 0:
					lista.append(number)
				
			for contador, x in enumerate(lista, 1):
				print(f"{contador}: {x}")
		case _:
			print('não existe opcao')

print("""
opcoes disponíveis:
1. gerar apenas números sem nenhum filtro
2. gerar apenas números pares 
3. gerar apenas números impares
""")
print(' ')
choice = input("digite oq vai ser: ")

quanti = int(input("quantos numeros vão ser gerados: "))

opcoes = {
	'1': number_generation,
	'2': number_generation,
	'3': number_generation,
}
funcao_escolhida = opcoes.get(choice)
if funcao_escolhida:
	funcao_escolhida(quanti, choice)