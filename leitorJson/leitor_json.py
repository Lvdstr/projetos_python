import json
from pathlib import Path

def iterar_valores_Lista(value):
    if type(value) == list:
        return f"{value[0]}, {value[1]}"
    else:
        return value


class Json():
    def __init__(self, arquivo_name, use_mode):
        self.arquivo_nome = arquivo_name
        self.use_mode = use_mode

    #usa a biblioteca pathlib para identificar a extensão do arquivo
    def IdentificarExtensao(self):
        file_path = Path(self.arquivo_nome)
        extension = file_path.suffix
        return extension


    #le o arquivo, básicão memo
    def AbrirJson(self):
        sasa = self.IdentificarExtensao()
        if sasa == ".json":
            with open(self.arquivo_nome, self.use_mode) as arquivo:
                arquivo_legível = json.load(arquivo)
                return arquivo_legível[0]
        else:
            print(f"esse arquivo é do tipo {sasa},\nfoi maus ai menó, so jeison aqui")
    
    def PercorrerChaves(self):
        chavesJson = []
        JsonPuro = self.AbrirJson()
        Chaves = JsonPuro.keys()
        for x in Chaves:
            chavesJson.append(x)
        return [JsonPuro, chavesJson]
    
    def arquivoNormal(self, conteudo):
        with open("sasa.txt", "a") as new:
            for x in conteudo:
                new.write(x)
    
    def leiturasasa(self):
        nada = []
        # pega a lista do return 
        value = self.PercorrerChaves()
        #atribuindo cada um dos itens a uma variavel diferente
        index1 = value[0] # index1 = JsonPuro
        index2 = value[1] # index2 = chavesJson
        for x in index1:
            a = f"{x}: {index1[x]}"
            nada.append(a + "\n")
            print(a)
        self.arquivoNormal(nada)

teste = Json("sukuna.json", "r")
teste.leiturasasa()