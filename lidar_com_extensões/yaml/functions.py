from os import name, system
from pathlib import Path


def IdentificarExtensao(value):
    """usa a biblioteca pathlib para verificar qual a extensâo do arquivo, e depois retorna a extensão"""
    file_path = Path(value)
    extension = file_path.suffix
    return extension


def iterar_valores_Lista(value):
    if type(value) == list: return f"{value[0]}, {value[1]}"
    else: return value


def limpar_terminal():
    match name:
        case "nt": system("cls")
        case _: system("clear")