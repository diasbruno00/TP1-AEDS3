from PIL import Image
from graph import Graph

g = Graph()

def imprimirGrafo(grafo):
    for no in grafo:
        print(no)

def criarGrafoMatriz(pixels):
   
   grafo = []
   width, height = img.size

   for i in range(height):
       coordenadas = []
       for j in range(width):
           if pixels[i] != (0, 0, 0):  # verificando se o pixel e preto
               coordenadas.append([i, j])
               for di in [-1, 0, 1]:
                  for dj in [-1, 0, 1]:
                       # mesma linha                                 # mesma coluana                 # != de preto
                      if 0 <= i + di < len(pixels) and 0 <= j + dj < len(pixels[0]) and pixels[i + di][j + dj] != (0, 0, 0):
                           coordenadas.append([i + di, j + dj])
       grafo.append(coordenadas)

   return grafo


#nomeArquivo = str(input('Informe o arquivo bitmap: '))

# Processamento 
img = Image.open('img.bmp')

# Converta a imagem para RGB


grafo = criarGrafoMatriz(pixels)

imprimirGrafo(grafo)

#print(grafo[0][4])
       # if pixels[i] != (0, 0, 0):

