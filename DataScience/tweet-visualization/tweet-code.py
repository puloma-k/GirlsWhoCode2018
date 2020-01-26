import json

file = open("tweets-small.json", "r")

tweet_data = json.load(file)

file.close()

# iterate through list using indices

for idx in range(len(tweet_data)):
    print("Text: ", tweet_data[idx]["text"])
    print(' ')

# iterate through list using element

for tweet in tweet_data:
    print("Text: ", tweet["text"])
    print(' ')
