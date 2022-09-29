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
  distancia = {}
  # vai armazenar todas as cidades e marcar com true os vizinhos
  vizinhos = {}

  bfs_traversal_output = []
  # O BFS é baseado em fila, portanto, usando 'Queue' do python embutido
  borda = Queue()

  # viajando pelas cidades no mapa e setando
  for cidade in mapaDaRomania.grafo.keys():
    # uma vez que inicialmente nenhuma cidade é visitada, então não haverá nada na lista visitada
    explorados[cidade] = False
    vizinhos[cidade] = None
    # setando as distancias em -1
    distancia[cidade] = -1

  # Começando
  startingCity = startingNode
  # Já foi explorado, pois começamos nela
  explorados[startingCity] = True
  # setando a distancia da cidade origem
  distancia[startingCity] = 0
  borda.put(startingCity)

  while not borda.empty():
    u = borda.get()  # pegando primeiro elemento da fila
    bfs_traversal_output.append(u)

    # explore as transições que saem do estado u
    for v in mapaDaRomania.grafo[u]:
      if not explorados[v]:
        explorados[v] = True
        vizinhos[v] = u
        distancia[v] = distancia[u] + 1
        borda.put(v)

  # chegar à nossa cidade de destino,
  g = destinationNode
  rota = []
  while g is not None:
    # adicionando cidade na rota
    rota.append(g)
    g = vizinhos[g]

  rota.reverse()
  # imprimindo o caminho para nossa cidade de destino
  print(rota)


# Chamando função de Busca em largura com cidade de inicio & cidade de destino
bfs(estado.estadoOrigem, destino.estadoDestino)
