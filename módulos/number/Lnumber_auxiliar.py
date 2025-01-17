from os import system, name


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


def verificação2(values):
    if values[0].isdigit() == False:
        return f"o valor {values[0]} não é um numero, se fodeu"
    else:
        return f"o valor {values[0]} não é um numero, se fodeu"