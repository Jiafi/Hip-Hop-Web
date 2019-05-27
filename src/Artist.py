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
  def create_graph_bfs(self, artist_limit=10, song_limit=20):
    artist_queue = queue.Queue()
    artist_queue.put(self.name)
    visited = set()
    visited_songs = set()
    while(len(visited) <= artist_limit and not artist_queue.empty()):
      current_artist = artist_queue.get()
      visited.add(current_artist)
      artist = genius.search_artist(current_artist, max_songs=song_limit, sort='popularity')
      # Get artists associated with current artist
      for song in artist.songs:
        # Do not want to repeat songs, waste of processing
        if (song.title not in visited_songs):
          visited_songs.add(song.title)
          # Add to queue in this block such that queue is by popularity of the song
          # it adds weight to edges based on # of features
          current_features = set()
          for feature in song.featured_artists:
            current_features.add(feature['name'])
          #for feature in song.producers:
            #current_features.add(feature['name'])

          # Create tuples to add edges
          # add features to graph
          # Done processing features
          for feature in current_features:
            # Adding edges and to the queue
            self.__increment_edge(current_artist, feature)
            if feature not in visited:
              artist_queue.put(feature)

  def show_graph(self):

    plt.subplot(121)

    plt.figure(figsize=(18.5, 11.5))
    plot = nx.draw(self.__graph, with_labels=True)
    plt.show()

  def __increment_edge(self, source, dest):
    edge = self.__graph.get_edge_data(source, dest)
    if edge is None:
      self.__graph.add_edge(source, dest, weight=1)
    else:
      self.__graph.add_edge(source, dest, weight=edge['weight']+1)
    print(self.__graph.get_edge_data(source, dest))

if __name__ == "__main__":
  genius = lyricsgenius.Genius("Ac918_2foSjtvsZXSydkug3UIGI3cUerNAVVkdhPDsZKM5gbOBkuiRmrXRjtGhmD")
  kanye = Artist("Kanye West", genius)
  kanye.create_graph_bfs()
  kanye.show_graph()
#madlib = Artist("Madlib", genius)
#madlib.create_graph_bfs(2)
#madlib.show_graph()
