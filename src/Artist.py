#!/usr/bin/env python

import lyricsgenius
genius = lyricsgenius.Genius("Ac918_2foSjtvsZXSydkug3UIGI3cUerNAVVkdhPDsZKM5gbOBkuiRmrXRjtGhmD")
#artist = genius.search_artist("Kanye West", sort="popularity", max_songs=3)
#songs = artist.songs
#for artist in songs[0].producers:
#print(artist)
song = genius.search_song('no more parties in la', 'Kanye West')
print(song.producers)

class Artst:

  def __init__(self, name, genius):
    self.name = name
    # artists is the vertex set for the graph, includes the artist we are starting with
    self.__artists = set([name])
    # genius api object expected
    self.__genius = genius

  def
