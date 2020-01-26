import music
import matplotlib.pyplot as plt
from wordcloud import WordCloud

list_of_music = music.get_songs()

artists_from_year = []

for ele in list_of_music:
    year = 2007
    if (ele["song"]["year"] == year):
        artists_from_year.append(ele["artist"]["name"])

# print(artists_from_2007)

artists = {}

for artist_name in artists_from_year:
    if artist_name not in artists:
        artists[artist_name] = 1
    else:
        artists[artist_name] += 1

print(artists)

wordcloud = WordCloud().generate_from_frequencies(artists)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
