from yaml import load, FullLoader
from functions import *


caminho = "yaml/saas.yaml"

def ler_yaml():
    try:
        verificar = IdentificarExtensao(caminho)
        if verificar == ".yaml":
            with open(caminho, "r") as arquivo:
                sate = load(arquivo, Loader=FullLoader)
            for x in sate:
                print(sate[x])
        else:
            print("o arquivo passado não é um arquivo yaml, caralho")
    except FileNotFoundError:
        print("arquivo não encontrando\nprograma encerrado")

limpar_terminal()
ler_yaml()