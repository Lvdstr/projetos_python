from pathlib import Path
from os import system, name


error_mensage = "infelizmente o arquivo passado não é um json"


def IdentificarExtensao(name):
    """
usa a biblioteca pathlib para verificar qual a extensâo do arquivo, 
e depois retorna a extensão
    """
    file_path = Path(name)
    extension = file_path.suffix
    if extension == ".json":
        return extension
    else:
        print(error_mensage)
        return


def list_convert(value):
    if type(value) == list:
        sasa = ", ".join(value)
        return sasa
    else:
        return value


def limpar_terminal():
    match name:
        case "nt": system("cls")
        case _: system("clear")