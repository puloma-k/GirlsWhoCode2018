import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Get the JSON data
tweet_file = open("tweets-small.json", "r")
tweet_data = json.load(tweet_file)
tweet_file.close()

tweet_polarity = []
tweet_subjectivity = []

for tweet in tweet_data:
    text = TextBlob(tweet["text"])
    tweet_polarity.append(text.sentiment.polarity)
    tweet_subjectivity.append(text.sentiment.subjectivity)

combined_tweets = ""

for tweet in tweet_data:
    combined_tweets += tweet["text"]

tweetblob = TextBlob(combined_tweets)

words_to_filter = ["about", "https", "automation", "from", "thing", "could", "they", "randazzoj", "gotta", "will"]

filtered_dictionary = {}

for word in tweetblob.words:
    print(word)
    if len(word) < 4:
        continue
    if not word.isalpha():
        continue
    if word.lower() in words_to_filter:
        continue
    if len(word) < 5 and word.upper() != word:
        continue
    filtered_dictionary[word.lower()] = tweetblob.word_counts[word.lower()]

wordcloud = WordCloud().generate_from_frequencies(filtered_dictionary)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()



# for idx in range(len(tweet_polarity)):
#     print("Text: ", tweet_data[idx]["text"])
#     print("P: ", tweet_polarity[idx])
#     print("S: ", tweet_subjectivity[idx])
#     print("\n")
#
# print("Avg polarity: ", sum(tweet_polarity) / len(tweet_polarity))
# print("Avg subjectivity: ", sum(tweet_subjectivity) / len(tweet_subjectivity))

# plt.hist(tweet_polarity, bins=[-1, -0.5, -0.25, 0.0, 0.25, 0.5, 1.0])
# plt.xlabel("Polarity")
# plt.ylabel("Number of Tweets")
# plt.title("Histogram of Tweet Polarity")
# plt.axis([-0.6, 1.0, 0, 80])
# plt.grid(True)
# plt.show()
#
# plt.hist(tweet_subjectivity, bins=[-1, -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1.0])
# plt.xlabel("Subjectivity")
# plt.ylabel("Number of Tweets")
# plt.title("Histogram of Tweet Subjectivity")
# plt.axis([0, 1, 0, 80])
# plt.grid(True)
# plt.show()
