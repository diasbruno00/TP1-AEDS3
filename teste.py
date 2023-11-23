from PIL import Image
import networkx as net
import matplotlib.pyplot as plt

def adicionarCoordenadasGrafo(G):
# Adicione os nós ao grafo
    for y in range(height):
        for x in range(width):
            G.add_node((y, x))

def validacaoArestaGrafo(G):
# Adicione as arestas ao grafo
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

def matrizAdjacencia(G):
    g = net.adjacency_matrix(G)
    g = g.toarray()
    return g



def imprimirGrafo(G):
    plt.figure(1)
    net.draw_networkx(G, pos=net.spring_layout(G), with_labels=True)
    plt.show()


if __name__ == "__main__":
    # Abra a imagem
    img = Image.open('img.bmp')

    img_rgb = img.convert('RGB')

    # Obtenha os pixels da imagem
    pixels = list(img_rgb.getdata())

    # Obtenha as dimensões da imagem
    width, height = img.size

    # Crie um grafo vazio
    G = net.Graph()

    adicionarCoordenadasGrafo(G)

    validacaoArestaGrafo(G)
