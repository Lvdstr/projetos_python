from os import system, name


def limpar_terminal():
    match name:
        case "nt": system("cls")
        case _: system("clear")