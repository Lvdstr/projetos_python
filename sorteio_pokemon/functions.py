from os import name, system


def iterar_valor_lista(value):
    """formata as evoluções de um pokemon retornado do json dadosPokemon
    para em vez de ser printado assim:
        ["nivel 16: iyvsaur", "nivel 32: venusaur"]
    seja assim:
        nivel 16: ivysaur
        nivel 32: venusaur"""
    if type(value) == list:
        return f"{value[0]}, {value[1]}"
    else:
        return value


def limpar_terminal():
    """
    função básica pra limpar o terminal independente do sistema
    operacional
    """
    if name == "nt": system("cls")
    else: system("clear")


def limpeza_de_caracteres(texto):
    """
    remove o caracter especial de quebra de linha \n que é adicionado
    em uma lista que foi criada usando o método readlines(), que é um
    metodo de manipulaçaõ de arquivos
    """
    caracteres_para_remover = "\n"
    return ''.join([char for char in texto if char not in caracteres_para_remover])