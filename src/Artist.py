#!/usr/bin/env python

import lyricsgenius
import networkx as nx

class Artist:

  def __init__(self, name, genius):
    self.name = name
    # artists is the vertex set for the graph, includes the artist we are starting with
    self.__artists = set([name])
    # genius api object expected
    self.__genius = genius
    self.__graph = nx.Graph()
    self.__graph.add_node(name)

  def  create_graph_dfs(self, limit):
    queue = Queue(maxsize=limit)
    queue.put(self.name)
    visited = set()
    while(len(self.__artists) <= limit):
      current_artist = queue.get()
      visited.add(current_artist)
      current_features = set()
      artist = genius.search_artist(current_artist, max_songs=20)
      for(song in artist.songs):


genius = lyricsgenius.Genius("Ac918_2foSjtvsZXSydkug3UIGI3cUerNAVVkdhPDsZKM5gbOBkuiRmrXRjtGhmD")
kanye = Artist("kanye", genius)
