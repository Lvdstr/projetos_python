import json
from os import system

def iterar_valores_Lista(value):
    """se o parâmetro passado for to tipo lista, retorna uma versão formatada do itens"""
    if type(value) == list:
        return f"{value[0]}, {value[1]}"
    else:
        return value


def sasa(archive, type):
    system("cls")
    try:
        with open(archive, "r") as arquivo:
            sasa = json.load(arquivo)

        if type == "{":
            #iterar sobre objetos no estilo chave ùnica
            quanti = sasa.keys()
            for x in quanti:
                print(sasa[x])


        elif type == "[":
            #iterar sobre varios objetos no estilo lista
            for x in sasa:
                print(x)


        elif type == " ":
            #iterar sobre um objeto ùnico
            for x in sasa:
                print(f"{x}, {iterar_valores_Lista(sasa[x])}")
                 
    except FileNotFoundError:
        print("arquivo inexistente, vidoca")


def morte():
    vida = input("digite o nome do arquivo json: ")
    vido = input("digite o tipo de json: ")
    sasa(vida, vido)

morte()