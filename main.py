from PIL import Image
import networkx as net
from collections import deque
import matplotlib.pyplot as plt

listaDeNosPretos = []


def busca_em_largura(G, inicio, alvo):
    fila = deque([(inicio, [])])
    visitados = set()

    while fila:
        no, caminho = fila.popleft()
        if no == alvo:
            return caminho
        if no not in visitados:
            visitados.add(no)
            vizinhos = list(G.neighbors(no))
            fila.extend((vizinho, caminho + [vizinho]) for vizinho in vizinhos)
    
    return None


def imprimir_direcoes(caminho, no_vermelho):
    for passo in caminho:
        if passo[0] < no_vermelho[0]:
            print("↑", end=" ")
        elif passo[0] > no_vermelho[0]:
            print("↓", end=" ")
        elif passo[1] < no_vermelho[1]:
            print("←", end=" ")
        elif passo[1] > no_vermelho[1]:
            print("→", end=" ")
        no_vermelho = passo
    print()

def adicionarCoordenadasGrafo(G):
# Adicione os nós ao grafo
    width, height = img.size
    for y in range(height):
        for x in range(width):
            G.add_node((y, x))

def validacaoArestaGrafo(G,pixels):
# Adicione as arestas ao grafo
    width, height = img.size  
    for y in range(height):
        for x in range(width):
            # Verifique os vizinhos (cima, baixo, esquerda, direita)
            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ny, nx = y + dy, x + dx
                # Certifique-se de que os vizinhos estão dentro dos limites da imagem
                if 0 <= ny < height and 0 <= nx < width:
                    # Verifique se nenhum dos dois pixels é preto
                    if pixels[y * width + x] != (0, 0, 0) and pixels[ny * width + nx] != (0, 0, 0):
                        G.add_edge((y, x), (ny, nx), weight=1)
                    else: 
                        listaDeNosPretos.append((y,x))
                

                
def buscarCorVemelhaAndRetornaCoordenada(pixels):
    width, height = img.size
    for y in range(height):
        for x in range(width):
            if pixels[y * width + x] == (255, 0, 0):
                return (y, x)
    return None

def buscarCorVerdeAndRetornaCoordenada(pixels):
    width, height = img.size
    for y in range(height):
        for x in range(width):
            if pixels[y * width + x] == (0, 255, 0):
                return (y, x)
    return None





if __name__ == "__main__":

    
    print(f'Observação: Não é necessário informar a extensão do arquivo \n')

    nomeArquivo = str(input('Informe o arquivo bitmap: '))
    print("\n")

    nomeArquivo = nomeArquivo +".bmp"
   
    img = Image.open(nomeArquivo)

    img_rgb = img.convert('RGB')

    pixels = list(img_rgb.getdata())

    G = net.Graph()

    print("Processando... \n")

    adicionarCoordenadasGrafo(G)
    validacaoArestaGrafo(G,pixels)

    no_vermelho = buscarCorVemelhaAndRetornaCoordenada(pixels)
    no_verde = buscarCorVerdeAndRetornaCoordenada(pixels)
    
    if no_vermelho is not None and no_verde is not None:
        caminho = busca_em_largura(G, no_vermelho, no_verde)
        if caminho is not None:
            print("É possivel deslocar o equipamento: \n")
            imprimir_direcoes(caminho, no_vermelho)
        else:
            print("Não é possível descolar esse equipamento. \n")
     


    

