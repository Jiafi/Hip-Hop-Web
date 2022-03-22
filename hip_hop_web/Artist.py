#!/usr/bin/env python

import lyricsgenius
import networkx as nx
import matplotlib.pyplot as plt
import queue
import os


class Artist:
    def __init__(self, name, genius):
        self.name = name
        # artists is the vertex set for the graph, includes the artist we are starting with
        self.__artists = set([name])
        # genius api object expected
        self.__genius = genius
        self.graph = nx.Graph()
        self.graph.add_node(name)

    # BFS with additional processing to create edges and other info
    # BFS will show more closely related artists than DFS
    def create_graph_bfs(self, artist_limit=10, song_limit=20):
        artist_queue = queue.Queue()
        artist_queue.put(self.name)
        visited = set()
        visited_songs = set()
        while len(visited) <= artist_limit and not artist_queue.empty():
            current_artist = artist_queue.get()
            visited.add(current_artist)
            artist = self.__genius.search_artist(
                current_artist, max_songs=song_limit, sort="popularity"
            )
            # Get artists associated with current artist
            for song_object in artist.songs:
                # Do not want to repeat songs, waste of processing
                song = song_object.to_dict()
                if song["title"] not in visited_songs:
                    visited_songs.add(song["title"])
                    # Add to queue in this block such that queue is by popularity of the song
                    # it adds weight to edges based on # of features
                    current_features = set()
                    for feature in song["featured_artists"]:
                        current_features.add(feature["name"])
                    for feature in song["producer_artists"]:
                        current_features.add(feature["name"])

                    # Create tuples to add edges
                    # add features to graph
                    # Done processing features
                    for feature in current_features:
                        # Adding edges and to the queue
                        self.__increment_edge(current_artist, feature)
                        if feature not in visited:
                            artist_queue.put(feature)

    def create_graph_dfs(self, artist_limit=10, song_limit=20):
        artist_stack = []
        artist_stack.append(self.name)
        visited = set()
        visited_songs = set()
        while len(visited) <= artist_limit and artist_stack:
            current_artist = artist_stack.pop()
            visited.add(current_artist)
            artist = self.__genius.search_artist(
                current_artist, max_songs=song_limit, sort="popularity"
            )
            # Get artists associated with current artist
            for song_object in artist.songs:
                song = song_object.to_dict()
                # Do not want to repeat songs, waste of processing
                if song["title"] not in visited_songs:
                    visited_songs.add(song["title"])
                    # Add to queue in this block such that queue is by popularity of the song
                    # it adds weight to edges based on # of features
                    current_features = set()
                    for feature in song["featured_artists"]:
                        current_features.add(feature["name"])
                    for feature in song["producer_artists"]:
                        current_features.add(feature["name"])

                    # Create tuples to add edges
                    # add features to graph
                    # Done processing features
                    for feature in current_features:
                        # Adding edges and to the queue
                        self.__increment_edge(current_artist, feature)
                        if feature not in visited:
                            artist_stack.append(feature)

    def show_graph(self):

        plt.subplot(121)

        plt.figure(figsize=(18.5, 11.5))
        plot = nx.draw(self.graph, with_labels=True)
        plt.show()

    def __increment_edge(self, source, dest):
        edge = self.graph.get_edge_data(source, dest)
        if edge is None:
            self.graph.add_edge(source, dest, weight=1)
        else:
            self.graph.add_edge(source, dest, weight=edge["weight"] + 1)
        print(self.graph.get_edge_data(source, dest))


if __name__ == "__main__":
    genius_token = os.environ.get("GENIUS_TOKEN")
    genius = lyricsgenius.Genius(genius_token)
    kanye = Artist("Kanye West", genius)
    # kanye.create_graph_bfs()
    kanye.create_graph_dfs(artist_limit=100, song_limit=100)
    kanye.show_graph()
