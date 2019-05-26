#!/usr/bin/env python

import lyricsgenius
import networkx as nx
import matplotlib.pyplot as plt
import queue
class Artist:

  def __init__(self, name, genius):
    self.name = name
    # artists is the vertex set for the graph, includes the artist we are starting with
    self.__artists = set([name])
    # genius api object expected
    self.__genius = genius
    self.__graph = nx.Graph()
    self.__graph.add_node(name)

  # BFS with additional processing to create edges and other info
  # BFS will show more closely related artists than DFS
  def create_graph_bfs(self, limit):
    artist_queue = queue.Queue()
    artist_queue.put(self.name)
    visited = set()
    while(len(self.__artists) <= limit and not artist_queue.empty()):
      current_artist = artist_queue.get()
      visited.add(current_artist)
      current_features = set()
      artist = genius.search_artist(current_artist, max_songs=2, sort='popularity')
      # Get artists associated with current artist
      for song in artist.songs:
        for feature in song.featured_artists:
          current_features.add(feature['name'])
        for feature in song.producers:
          current_features.add(feature['name'])

      # Create tuples to add edges
      edges = []
      for feature in current_features:
        # Adding edges and to the queue
        print(feature)
        if feature not in visited:
          artist_queue.put(feature)
        edges.append((current_artist, feature))
      # add features to graph
      self.__graph.add_edges_from(edges)
      # Done processing features

  def show_graph(self):
    plt.subplot(121)
    nx.draw(self.__graph, with_labels=True)
    plt.show()

genius = lyricsgenius.Genius("Ac918_2foSjtvsZXSydkug3UIGI3cUerNAVVkdhPDsZKM5gbOBkuiRmrXRjtGhmD")
kanye = Artist("kanye west", genius)
kanye.create_graph_bfs(5)
kanye.show_graph()
