from queue import Queue
from Classes import Transicao, Estado, Mapa

# instanciando classes
estado = Estado.Estado()
destino = Transicao.Transicao()
mapaDaRomania = Mapa.Mapa()


def bfs(startingNode, destinationNode):
  # Para acompanhar o que visitamos
  explorados = {}
  # manter o controle de distância
  distance = {}
  # nó pai do gráfico específico
  parent = {}

  bfs_traversal_output = []
  # O BFS é baseado em fila, portanto, usando 'Queue' do python embutido
  borda = Queue()

  # viajando pelas cidades no mapa
  for city in mapaDaRomania.grafo.keys():
    # uma vez que inicialmente nenhuma cidade é visitada, então não haverá nada na lista visitada
    explorados[city] = False
    parent[city] = None
    # setando as distancias em -1
    distance[city] = -1

  # Começando
  startingCity = startingNode
  # Já foi explorado
  explorados[startingCity] = True
  # setando a distancia da cidade origem
  distance[startingCity] = 0
  borda.put(startingCity)

  while not borda.empty():
    u = borda.get()  # ppegando rimeiro elemento da fila
    bfs_traversal_output.append(u)

    # explore as transições que saem do estado u
    for v in mapaDaRomania.grafo[u]:
      if not explorados[v]:
        explorados[v] = True
        parent[v] = u
        distance[v] = distance[u] + 1
        borda.put(v)

  # chegar à nossa cidade de destino,
  g = destinationNode
  rota = []
  while g is not None:
    # adicionando cidade na rota
    rota.append(g)
    g = parent[g]

  rota.reverse()
  # imprimindo o caminho para nossa cidade de destino
  print(rota)


# Chamando função de Busca em largura com cidade de inicio & cidade de destino
bfs(estado.estadoOrigem, destino.estadoDestino)
