from PIL import Image
import networkx as net
from collections import deque
import tkinter as tk
from tkinter import filedialog
from PIL import ImageDraw


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
                ny, net = y + dy, x + dx
                # Certifique-se de que os vizinhos estão dentro dos limites da imagem
                if 0 <= ny < height and 0 <= net < width:
                    # Verifique se nenhum dos dois pixels é preto
                    if pixels[y * width + x] != (0, 0, 0) and pixels[ny * width + net] != (0, 0, 0):
                        G.add_edge((y, x), (ny, net), weight=1)
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


def escolher_arquivo():
    root = tk.Tk()
    root.withdraw()
    root.title("Escolha seu arquivo")
    arquivo = filedialog.askopenfilename()
    return arquivo

def exibir_imagem_atualizada(img, caminho):
    img_copy = img.copy()
    draw = ImageDraw.Draw(img_copy)
    
    for node1, node2 in zip(caminho, caminho[1:]):
        draw.line([node1[::-1], node2[::-1]], fill=(255, 0, 127), width=5)  
 
    img_copy.show()


if __name__ == "__main__":

    try:
        print('Selecione o arquivo: \n')
        nomeArquivo = escolher_arquivo()

        print(f'Arquivo selecionado: {nomeArquivo} \n')

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
                #imprimir_direcoes(caminho, no_vermelho)
                exibir_imagem_atualizada(img, caminho)
               
            else:
                print("Não é possível descolar esse equipamento. \n")
        
    except FileNotFoundError as e:
        print(f' Arquivo {nomeArquivo} não encontrado no diretorio')
    except Exception as e:
        print(f'Erro inesperado {e}')
    

