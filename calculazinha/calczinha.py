from modulo_calc import *

def repetir_codigo():
	repetir = input("deseja repetir o código: ")
	if repetir == "s":
		iniciar()
	else:
		print("témais")
		sleep(0.7)
		verificar_sistema()


def options(opcao):
	funco = [ calc_basica, calc_porcentagi, calc_desconto, calc_media, calc_medidas ]
	
	if opcao in ["1", "2", "3"]:
		value_one = float(input("digite o 1 numero: "))
		value_two = float(input("digite o 2 numero: "))
	
	match opcao:
		case '1': funco[0](value_one, value_two)
		case '2': funco[1](value_one, value_two)
		case '3': funco[2](value_one, value_two)
		case '4': funco[3]()
		case '5': funco[4]()


def iniciar():
	print("""
1- calculadora de operações aritiméticas
2- calculadora de porcentagem
3- calculadora de desconto
4- calculadora de média de notas
5- conversor de centimetros para metros
	""")

	calc_choose = input("digite o numero da calculadora que deseja utilizar: ")

	options(calc_choose)
	repetir_codigo()

iniciar()