from tinydb import TinyDB, Query

lista = []
db = TinyDB('historico.json')

def registrar_banco(registro):
	db.insert({"conta_realizada:": registro})

def calc_basica(valor1, valor2):
	database = TinyDB('caculadora1.json')
	operacao = input('''
escolha a operacao
+ para adicao
- para subtracao
* para multiplicacao
/ para divisao
% para modulo
// para divisao minima
** para exponencial:
''')
	
	operações = {
		"+": valor1 + valor2,
		"-": valor1 - valor2,
		"*": valor1 * valor2,
		"/": valor1 / valor2,
		"**": valor1 * valor2,
		"//": valor1 // valor2,
		"%": valor1 % valor2
	}
	
	print(f"{valor1} {operacao} {valor2} = {operações.get(operacao)}")
	result = f"{valor1} {operacao} {valor2}"
	registrar_banco(result)


def calc_porcentagi(valor1, valor2):
	database = TinyDB('caculadora2.json')
	print("""
esta calculadora oferece opções
relacionadas a cálculo de porcentagem de
um valor:
1-calcular a porcentagem de um numero
2-descobrir quantos porcento um numero é
de outro\n
""")
	pergunta = int(input("escolha uma opção:"))
	if pergunta == 1:
		operacao = valor2 * valor1 / 100
		result = f"{valor2} % de {valor1} = {operacao}%"
		print(result)
		registrar_banco(result)
	
	elif pergunta == 2:		
		operacao = valor2 / valor1 * 100
		result = f"{valor2} equivale a {operacao}% de {valor1}"
		print(result)
		registrar_banco(result)

def calc_desconto(valor1, valor2):
	database = TinyDB('caculadora3.json')
  print("Calcule o valor de um produto com desconto")
  valor_com_desconto = valor1 - (valor1 * valor2 / 100)
  result = f"{valor1} menos {valor2} % = {valor_com_desconto}"
  registrar_banco(result)
  print(f"Esse é o valor do produto com desconto: {valor_com_desconto}$ reais")

def calc_media():
	database = TinyDB('caculadora4.json')
	quanti_notas = int(input("digite quanto notas ira calcular: "))
	for x in range(quanti_notas):
		x += 1
		notas = float(input(f"digite a {x} nota: "))
		lista.append(notas)
	
	resultado = sum(lista) / len(lista)
	result = f"a media de {len(lista)} notas = {resultado}"
	registrar_banco(result)
	print(f"a media de {len(lista)} notas eh {resultado}")

def calc_medidas():
	database = TinyDB('caculadora5.json')
	number = int(input("digite um valor para ser convertido: "))
	metros_for_centimetros = float(input("""
deseja converter:
1- metros para centímetros
2- centímetros para metros
"""))
	if metros_for_centimetros == 1:
		metros = number / 100
		print(f"{number} centímetros convertidos dão {metros} metros")
    	
	if metros_for_centimetros == 2:
		metros = number * 100
		print(f"{number} metros convertidos dão {metros} centímetros")