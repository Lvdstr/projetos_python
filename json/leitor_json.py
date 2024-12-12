import json
from pathlib import Path
from colorama import Fore


def iterar_valores_Lista(value):
    if type(value) == list:
        return f"{value[0]}, {value[1]}"
    else:
        return value


class Json():
    """
    """
    def __init__(self, arquivo_name, use_mode):
        self.arquivo_nome = arquivo_name
        self.use_mode = use_mode

    def __str__(self):
        print("em contrução")


    def IdentificarExtensao(self):
        """usa a biblioteca pathlib para verificar qual a extensâo do arquivo, e depois retorna a extensão"""
        file_path = Path(self.arquivo_nome)
        extension = file_path.suffix
        return extension


    def AbrirJson(self):
        """tenta abrir o arquivo, chama a função de verificação, pra confirmar se o arquivo é json, retorna o arquivo para uma função que vai manipular esses dados"""
        try:
            with open(self.arquivo_nome, self.use_mode) as arquivo:
                arquivo_legível = json.load(arquivo)

            verificar = self.IdentificarExtensao()
            if verificar == ".json":
                return arquivo_legível
            else:
                print(f"esse arquivo é do tipo {verificar},\nfoi maus ai menó, so jeison aqui")

        except FileNotFoundError:
            print("erro zézinho")
    

    def arquivoNormal(self, conteudo):
        """cria um arquivo de texto normal com os valores do json"""
        with open("sasa.txt", "a") as new:
            for x in conteudo:
                new.write(x)
    

    def leiturasasa(self):
        """itera sobre os itens chave:valor do dicionario json, se for uma lista chama a função iterar pra formatar a impressão"""
        pegarJson = self.AbrirJson()
        for x in pegarJson:
            print(f"{Fore.YELLOW + x + Fore.RESET}: {iterar_valores_Lista(pegarJson[x])}")


teste = Json("jaison.json", "r")

teste.leiturasasa()

#exibe as docstrings dos métodos da classe
#print(teste.AbrirJson.__doc__)