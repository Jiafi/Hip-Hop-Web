import lyricsgenius
genius = lyricsgenius.Genius("Ac918_2foSjtvsZXSydkug3UIGI3cUerNAVVkdhPDsZKM5gbOBkuiRmrXRjtGhmD")
artist = genius.search_artist("Kanye West", sort="popularity")
print(artist.songs)
