from Aresta import Aresta
from Vertice import Vertice
import numpy as np
import csv
from os import read
from Grafo import *

fileVertices = open('Vertices.csv')
fileArestas = open('Arestas.csv')

vertices = []
for vertice in csv.reader(fileVertices):
  try:
    id = int(vertice[0].split(';')[0])
    nome = vertice[0].split(';')[1]
    vertices.append(Vertice(id, nome))
  except:
    print('')

aux_vertices = np.array(vertices)
arestas = []
for aresta in csv.reader(fileArestas):
  try:
    id = int(aresta[0].split(';')[0])

    idVerticeOrigem = [x for x in aux_vertices if x.id == int(aresta[0].split(';')[1])][0]
    idVerticeDestino = [x for x in aux_vertices if x.id == int(aresta[0].split(';')[2])][0]

    peso = float(aresta[0].split(';')[3])
    arestas.append(Aresta(id, idVerticeOrigem, idVerticeDestino, peso))
  except ValueError:
    print('')

grafo = Grafo(vertices, arestas)

grafo.imprimirAdjacentes()

# Plotar grafo

import networkx as nx

G = nx.DiGraph()

for vertice in vertices:
  G.add_node(vertice.id)

for aresta in arestas:
  G.add_edge(aresta.verticeOrigem.id, aresta.verticeDestino.id)

print("Nodes of graph: ")
print(G.nodes())
print("Edges of graph: ")
print(G.edges())

nx.draw(G)