from random import choice, randint
from json import load
from os import name, system
from tinydb import TinyDB, Query
from colorama import Fore
from functions import *


User = Query() #query para consultas
db = TinyDB('historico.json') #criação do banco de dados 


def item_exists(key, value):
    """
    verifica se existe um valor no banco de dados de pokemons
    sorteados que corresponde aquela chave
    """
    return db.contains(User[key] == value)


def exibir_dados(pokes):
    """
    abre o arquivo json, atribui ele a uma outra variavel,
    pega os valores de cada chave e joga em uma lista pra
    formatar sua exibição no terminal
    """
    with open('DadosPokemon.json', 'r', encoding='utf-8') as arquivo:
        dados = load(arquivo)

    pokemon = dados[pokes]
    evolucao = iterar_valor_lista(pokemon["evolução"])
    tipo = iterar_valor_lista(pokemon["tipo"])
    
    format = [
        f"nome: {Fore.GREEN + pokemon["nome"] + Fore.RESET}",
        f"tipo/s: {Fore.GREEN + tipo + Fore.RESET}",
        f"evolução/ões: {Fore.GREEN + evolucao + Fore.RESET}"
    ]

    for x in format:
        print(x)
    print(" ")


def formatar_dados(pokes):
    """
    recebe a lista de nomes de pokemons sorteados, chama a função
    de limpeza de caracteres e depois joga pra função de exibição
    """
    lista_limpa = []
    for x in pokes:
        new = limpeza_de_caracteres(x)
        lista_limpa.append(new)
    for x in lista_limpa:
        exibir_dados(x)


def abrir_arquivo(gen_choice):
    """
    abre o txt puro contendo o nome de cada um dos pokemons,
    realiza o sorteio de pokemons baseado no critério geracional
    ou seja sorteia pokemons correspondente a 1,2 ou todas as gerações
    """
    generations = {
        "1": [0, 151],
        "2": [152, 251],
        "3": [252, 386],
        "4": [387, 493],
        "5": [494, 649],
        "6": [650, 721],
        "7": [722, 809],
        "8": [810, 905],
        "9": [906, 932]
    }
    lista_filtrada = []
    with open("pokemons.txt", "r") as abrir_arquivo:
        lista_pokemons = abrir_arquivo.readlines()
        if gen_choice == "all":
            return lista_pokemons
        else:
            start = generations.get(gen_choice)
            stop = generations.get(gen_choice)
            start = start[0]
            stop = stop[1]
            for x in range(start, stop):
                item_atual = lista_pokemons[x]
                start += 1
                lista_filtrada.append(item_atual)
            return lista_filtrada


def registrarNoBanco(values):
    """
    verifica se o item ja existe no banco,
    se ja existir formata sua exibição em vermelho
    senão registra no banco e formata a exibição em verde
    """
    pokemons = []
    for x in values:
        pokemons.append(x)
        if item_exists("pokemon_sorteado", x):
            print(Fore.RED + x + Fore.RESET)
        else:
            db.insert({"pokemon_sorteado": x})
            print(Fore.GREEN + x + Fore.RESET)
    formatar_dados(pokemons)

	
def sortear_pokemons(quanti_pokes):
    """
    função inicial para começar o programa
    """
    itens_sorteados = []
    gen_choice = input("""
escolha:
1- primeira geração
2- segunda geração
3- terceira geração
4- quarta geração
5- quinta geração
6- sexta geração
7- sétima geração
8- oitava geração
9- nona geração
all- todas                  
""")
    if gen_choice in ["1","2","3","4","5","6","7","8","9","all"]:
        limpar_terminal()
        arquivo_nomes = abrir_arquivo(gen_choice)
    else:
        print(f"{gen_choice} não é uma opção válida. programa encerrado")
        limpar_terminal()
        return
    for x in range(quanti_pokes):
        pokemon_sorteado = choice(arquivo_nomes)
        itens_sorteados.append(pokemon_sorteado)
    registrarNoBanco(itens_sorteados)


quantidade = int(input("digite quantos pokemons vai sortear: "))
sortear_pokemons(quantidade)