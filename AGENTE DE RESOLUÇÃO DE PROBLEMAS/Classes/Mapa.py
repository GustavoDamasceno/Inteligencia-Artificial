class Mapa:
  def __init__ (self):
    self.grafo = {
      'Arad': ['Sibiu', 'Zerind', 'Timisoara'],
      'Zerind': ['Arad', 'Oradea'],
      'Oradea': ['Zerind', 'Sibiu'],
      'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu'],
      'Timisoara': ['Arad', 'Lugoj'],
      'Lugoj': ['Timisoara', 'Mehadia'],
      'Mehadia': ['Lugoj', 'Drobeta'],
      'Drobeta': ['Mehadia', 'Craiova'],
      'Craiova': ['Drobeta', 'Rimnicu', 'Pitesti'],
      'Rimnicu': ['Sibiu', 'Craiova', 'Pitesti'],
      'Fagaras': ['Sibiu', 'Bucharest'],
      'Pitesti': ['Rimnicu', 'Craiova', 'Bucharest'],
      'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
      'Giurgiu': ['Bucharest'],
      'Urziceni': ['Bucharest', 'Vaslui', 'Hirsova'],
      'Hirsova': ['Urziceni', 'Eforie'],
      'Eforie': ['Hirsova'],
      'Vaslui': ['Iasi', 'Urziceni'],
      'Iasi': ['Vaslui', 'Neamt'],
      'Neamt': ['Iasi']
    }