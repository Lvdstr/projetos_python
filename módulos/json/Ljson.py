__name__ = "moduloLocal_json"

from json import load
from os import system, name
from pathlib import Path
from colorama import Fore


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


def abrir_arquivo(caminho):
    with open(caminho, "r") as arquivo:
        json = load(arquivo)
    return json


def exibir_json(caminho):
    """
exibe o conteudo de um arquivo json que contem apenas um objeto
    """
    limpar_terminal()
    IdentificarExtensao(caminho)
    json = abrir_arquivo(caminho)

    for x in json:
        chave = x.capitalize()
        valor = list_convert(json[x])
        dados = f"{Fore.YELLOW + chave + Fore.RESET}: {valor}"
        print(dados)


def exibir_json_lista(caminho, item):
    """
exibe o conteudo de um arquivo json que segue o estilo lista de objetos
    """
    limpar_terminal()
    IdentificarExtensao(caminho)
    json = abrir_arquivo(caminho)

    for x in json:
        chave = x.capitalize()
        valor = list_convert(json[x])
        dados = f"{Fore.YELLOW + chave + Fore.RESET}: {valor}"
        print(dados)


def exibir_json_cv(caminho, item):
    """
exibe o conteudo de um arquivo json que segue o estilo chave única
    """
    limpar_terminal()
    IdentificarExtensao(caminho)
    json = abrir_arquivo(caminho)

    for x in json:
        chave = x.capitalize()
        valor = list_convert(json[x])
        dados = f"{Fore.YELLOW + chave + Fore.RESET}: {valor}"
        print(dados)


def gravar_json(caminho, novo_arquivo, tipo=None):
    """
escreve o conteudo de um objeto json em um arquivo txt
    """
    limpar_terminal()
    IdentificarExtensao(caminho)
    json = abrir_arquivo(caminho)

    novo = open(novo_arquivo, "w")
    for x in json:
        chave = x.capitalize()
        valor = list_convert(json[x])
        dados = f"{chave}: {valor}"
        novo.write(dados + "\n")
    novo.close()


def converter_json(caminho):
    """
transforma todas as chaves e valores de um objeto json em um dicionário python
    """
    limpar_terminal()
    IdentificarExtensao(caminho)
    json = abrir_arquivo(caminho)
    dados = dict(json)
    return dados