__name__ = "moduloLocal_number"

from json import load
from os import system, name
from colorama import Fore


def limpar_terminal():
    match name:
        case "nt": system("cls")
        case _: system("clear")


def verificação(value):
    limpar_terminal()
    if type(value) == int:
        return True
    elif type(value) == str:
        if value.isdigit() == True:
            value = int(value)
            return True
        else:
            return False


def sasa(values):
    if values[0].isdigit() == False:
        return f"o valor {values[0]} não é um numero, se fodeu"
    else:
        return f"o valor {values[0]} não é um numero, se fodeu"


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
        a = sasa([value1, value2])
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
        a = sasa([value1, value2])
        return a


print(operações_básicas("+", "a", 7))