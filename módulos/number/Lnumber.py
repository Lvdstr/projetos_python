__name__ = "moduloLocal_number"


from Lnumber_auxiliar import *


def operações_básicas(operator, value1, value2,):
    limpar_terminal()
    if verificação(value1) == True and verificação(value2) == True:
        value1 = int(value1)
        value2 = int(value2)
        match operator:
            case "+":
                return f"{value1} {operator} {value2} = {value1 + value2}"
            case "-":
                return f"{value1} {operator} {value2} = {value1 - value2}"
            case "/":
                try:
                    return f"{value1} {operator} {value2} = {value1 / value2}"
                except ZeroDivisionError:
                    return "erro detectado, tentátiva de divisão por zero"
            case "*":
                return f"{value1} {operator} {value2} = {value1 * value2}"
            case _:
                return f"erro, o operador {operator} não é válido"
    else:
        a = verificação2([value1, value2])
        return a


def fatorial(number):
    if number == 1 or number == 0:
        return 1
    return number * fatorial(number - 1)


def operações_avançadas(operator, value1="", value2=""):
    limpar_terminal()
    if verificação(value1) == True and verificação(value2) == True:
        value1 = int(value1)
        value2 = int(value2)
        match operator:
            case "**":
                return f"{value1} {operator} {value2} = {value1 ** value2}"
            case "//":
                return f"{value1} {operator} {value2} = {value1 // value2}"
            case "%": 
                return f"{value1} {operator} {value2} = {value1 % value2}"
            case "!":
                valor = fatorial(value1)
                return valor
            case _:
                return f"erro, o operador {operator} não é válido"
    else:
        a = verificação2([value1, value2])
        return a


def maior(value):
    limpar_terminal()
    for x in value:
        if type(x) == str:
            print("error")
        else:
            maior_valor = max(value)
    print(f" o maior valor é: {maior_valor}")


def menor(value):
    limpar_terminal()
    for x in value:
        if type(x) == str:
            print("error")
        else:
            maior_valor = min(value)
    print(f"o menor valor é: {maior_valor}")
