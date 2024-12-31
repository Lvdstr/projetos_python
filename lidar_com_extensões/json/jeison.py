from json import load
from os import system, name
from colorama import Fore
from pathlib import Path


__main__ = "moduloLocal_json"


def IdentificarExtensao(name):
    """usa a biblioteca pathlib para verificar qual a extensâo do arquivo, e depois retorna a extensão"""
    file_path = Path(name)
    extension = file_path.suffix
    return extension


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


def exibir_json(caminho):
    limpar_terminal()
    verificar = IdentificarExtensao(caminho)
    match verificar:
        case ".json":
            with open(caminho, "r") as arquivo:
                json = load(arquivo)


            for x in json:
                chave = x.capitalize()
                valor = list_convert(json[x])
                dados = f"{Fore.YELLOW + chave + Fore.RESET}: {valor}"
                print(dados)
        case _:
            print("infelizmente o arquivo passado não é um json")


def gravar_json(caminho, novo_arquivo):
        verificar = IdentificarExtensao(caminho)
        match verificar:
            case ".json":
                with open(caminho, "r") as arquivo:
                    json = load(arquivo)

                novo = open(novo_arquivo, "w")
                for x in json:
                    chave = x.capitalize()
                    valor = list_convert(json[x])
                    dados = f"{chave}: {valor}"
                    novo.write(dados + "\n")
                novo.close()
            case _:
                print("infelizmente o arquivo passado não é um json")