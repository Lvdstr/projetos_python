import json
from random import choice
from colorama import Fore, Style


def iterar_valoresLista(value):
    if type(value) == list:
        return f"{value[0]}, {value[1]}"
    else:
        return value

def ler_json(pokes):
    with open('sasa.json', 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)

    pokemon = dados[pokes]
    evolucao = iterar_valoresLista(pokemon["evolução"])
    tipo = iterar_valoresLista(pokemon["tipo"])
    
    format = [
        f"nome: {Fore.GREEN + pokemon["nome"] + Fore.RESET}",
        f"tipo/s: {Fore.GREEN + tipo + Fore.RESET}",
        f"evolução/ões: {Fore.GREEN + evolucao + Fore.RESET}"
    ]

    for x in format:
        print(x)
    print(" ")

def remove_caracteres_especificos(texto):
    caracteres_para_remover = "\n"
    return ''.join([char for char in texto if char not in caracteres_para_remover])


def malevolente(pokes):
    lista_limpa = []
    for x in pokes:
        new = remove_caracteres_especificos(x)
        lista_limpa.append(new)
    for x in lista_limpa:
        ler_json(x)