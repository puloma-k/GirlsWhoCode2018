import json
# from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import re


tweet_file = open("tweets-small.json", "r")
tweet_data = json.load(tweet_file)
tweet_file.close()

tweet_search = "automation"

# combine all text for all tweets into one string
combined_tweets = ""
for tweet in tweet_data:
    combined_tweets += tweet["text"]

cleaned_tweets = re.sub(r'[^\w\s]', '', combined_tweets)

words_to_filter = ["about", "https", "thing", "will", "could", "randazzoj", "gotta", "should", tweet_search]
filtered_words = []

for word in cleaned_tweets.split():
    if len(word) < 5:
        continue
    if not word.isalpha():
        continue
    if word.lower() in words_to_filter:
        continue
    filtered_words.append(word)

word_count = {}
for word in filtered_words:
    if word.lower() not in word_count:
        word_count[word.lower()] = 1
    else:
        word_count[word.lower()] += 1

print(word_count)

# WORDCLOUD STUFF
wordcloud = WordCloud().generate_from_frequencies(word_count)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
