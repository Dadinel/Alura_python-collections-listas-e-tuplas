def faz_processamento_de_visualizacao(lista):
    print(len(lista))
    #lista.append(13)

def faz_processamento_de_visualizacaoX(lista = []):
    print(len(lista))
    lista.append(13)

def faz_processamento_de_visualizacaoY(lista = None):
    if lista == None:
        lista = list()

    print(len(lista))
    lista.append(13)

idades = [16, 21, 29, 56, 43]

faz_processamento_de_visualizacao(idades)

print(idades)

faz_processamento_de_visualizacaoX()
faz_processamento_de_visualizacaoX()
faz_processamento_de_visualizacaoX()
faz_processamento_de_visualizacaoX()

faz_processamento_de_visualizacaoY()
faz_processamento_de_visualizacaoY()
faz_processamento_de_visualizacaoY()
faz_processamento_de_visualizacaoY()