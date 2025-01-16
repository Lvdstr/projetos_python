__name__ = "moduloLocal_json"


from json import load
from colorama import Fore
from Ljson_auxiliar import *


def abrir_arquivo(caminho):
    with open(caminho, "r") as arquivo:
        json = load(arquivo)
    return json


def sasa(caminho):
    limpar_terminal()
    IdentificarExtensao(caminho)
    json = abrir_arquivo(caminho)
    return json

    
def exibir_json(caminho):
    """
exibe o conteudo de um arquivo json que contem apenas um objeto
    """
    json = sasa(caminho)

    for x in json:
        chave = x.capitalize()
        valor = list_convert(json[x])
        dados = f"{Fore.YELLOW + chave + Fore.RESET}: {valor}"
        print(dados)


def gravar_json(caminho, novo_arquivo, tipo=None):
    """
escreve o conteudo de um objeto json em um arquivo txt
    """
    json = sasa(caminho)

    try:
        novo = open(novo_arquivo, "w")
        for x in json:
            chave = x.capitalize()
            valor = list_convert(json[x])
            dados = f"{chave}: {valor}"
            novo.write(dados + "\n")
        novo.close()
        print("arquivo criado com sucesso")
    except:
        print("erro na criação do arquivo")


def converter_json(caminho):
    """
transforma todas as chaves e valores de um objeto json em um dicionário python
    """
    json = sasa(caminho)
    dados = dict(json)
    return dados


def exibir_auxiliar(value):
    """
função auxiliar para formatar a exibição dos valores de um json que contem mais de um objeto
    """
    for x in value:
        print(f"{Fore.YELLOW + x + Fore.RESET}: {list_convert(value[x])}")
    print(" ")


def exibir_json_lista(caminho):
    """
exibe o conteudo de um arquivo json que segue o estilo lista de objetos
    """
    lista = []
    json = sasa(caminho)
    for x in json:
        lista.append(x)
    for x in lista:
        exibir_auxiliar(x)


def exibir_json_cv(caminho):
    """
exibe o conteudo de um arquivo json que segue o estilo chave única
    """
    lista = []
    json = sasa(caminho)
    a = json.keys()
    for x in json:
        item = json[x]
        lista.append(item)
    for x in lista:
        exibir_auxiliar(x)