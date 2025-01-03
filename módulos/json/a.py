from Ljson import *

#uso simples da biblioteca, exibindo dados
exibir_json("módulos/sukuna.json")

# teste básico de duas funções da biblioteca juntas
dicio = converter_json("sukuna.json")
for x in dicio:
    print(f"{x}: {list_convert(dicio[x])}")

#gravar conteudo em um arquivo separado
gravar_json("módulos/sukuna.json", "aa.txt")