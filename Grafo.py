import Aresta as aresta
import Vertice as vertice

class Grafo:
  def __init__(self, vertices, arestas):
    self.vertices = vertices
    self.verticesAdjacentes = self.setAdjacentes(vertices, arestas)

  def setAdjacentes(self, vertices, arestas):
    aux = []
    for i, vertice in enumerate(vertices):
      aux.append([])
      for aresta in arestas:
        if aresta.verticeOrigem.id == vertice.id:
          aux[i].append(aresta.verticeDestino)

    return aux
  
  def imprimirAdjacentes(self):
    for i, vertice in enumerate(self.vertices):
      adjacentes = ""
      for j, adjacente in enumerate(self.verticesAdjacentes[i]):
        adjacentes += adjacente.nome
        adjacentes += ", " if j < len(self.verticesAdjacentes[i]) - 1 else ""
      print(f'Adjacentes de {vertice.nome}: {adjacentes}')