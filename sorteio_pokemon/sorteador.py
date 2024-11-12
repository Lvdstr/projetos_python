from random import choice
from tinydb import TinyDB, Query
from colorama import Fore, Style
from os import name, system
from dados import iniciar_exibição

User = Query()
db = TinyDB('historico.json')

def limpar_terminal():
    if name == "nt":
        system("cls")
    else:
        system("clear")

def item_exists(key, value):
    return db.contains(User[key] == value)

def abrir_arquivo(number):
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
    try:
        abrir_arquivo = open("pokemons.txt", "r")
        lista_pokemons = abrir_arquivo.readlines()
        if number == "all":
            return lista_pokemons
        else:
            start = generations.get(number)
            stop = generations.get(number)
            start = start[0]
            stop = stop[1]
            for x in range(start, stop):
                item_atual = lista_pokemons[x]
                start += 1
                lista_filtrada.append(item_atual)
            return lista_filtrada
    except:
        print("erro")
    finally:
        abrir_arquivo.close

def registrarNoBanco(values):
    pokemons = []
    for x in values:
        pokemons.append(x)
        if item_exists("pokemon_sorteado", x):
            print(Fore.RED + x + Fore.RESET)
        else:
            db.insert({"pokemon_sorteado": x})
            print(Fore.GREEN + x + Fore.RESET)
    iniciar_exibição(pokemons)

	
def sortear_pokemons(quanti_pokes):
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
        print("sla")
        limpar_terminal()
        return
    for x in range(quanti_pokes):
        pokemon_sorteado = choice(arquivo_nomes)
        itens_sorteados.append(pokemon_sorteado)
    registrarNoBanco(itens_sorteados)


quantidade = int(input("digite quantos pokemons vai sortear: "))
sortear_pokemons(quantidade)