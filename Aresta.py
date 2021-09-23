class Aresta:
  def __init__(self, id, verticeOrigem, verticeDestino, peso):
    self.id = id
    self.verticeOrigem = verticeOrigem
    self.verticeDestino = verticeDestino
    self.peso = peso

  def __str__(self):
    return f'Origem: {self.verticeOrigem.nome} | Peso: {self.peso} | Destino: {self.verticeDestino.nome}'