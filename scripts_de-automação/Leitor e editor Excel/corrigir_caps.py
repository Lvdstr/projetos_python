from openpyxl import load_workbook


workbook = load_workbook("registros.xlsx")
planilha = workbook["MANGAS"]

def verifiy(value):
    jimmin = value.partition("c")
    nova_celula = "b" + jimmin[2]
    sla = planilha[value].value
    if sla > planilha[nova_celula].value:
        new_value = planilha[nova_celula] = planilha[value].value
        workbook.save("/data/data/com.termux/files/home/scripts/exceu/registros.xlsx")


def verificar():
    colunas = ["b", "c"]
    for x in range(2, 101):
        celula = colunas[1] + str(x)
        sasa = planilha[celula].value
        if sasa != None:
            verifiy(celula)

verificar()