import json
import pandas as pd
import re

tweets_data = []
tweets_file = open("./res.txt", "r")
tweets_lines = tweets_file.readlines()
for line in tweets_lines:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

# extract link function
def extract_link(text):
    regex = 'https?://[^\s<>"]+|www\.[^\s<>"]+'
    match = re.search(regex, text)
    if match:
        return match.group()
    return '' 

# parsing fields of text, location and link
# update fields of urls' titles later
tweets = pd.DataFrame()
tweets['text'] = list(map(lambda tweet: tweet['text'], tweets_data))
tweets['location'] = list(map(lambda tweet: tweet['place']['full_name'] if tweet['place'] != None else None, tweets_data))
tweets['link'] = tweets['text'].apply(lambda tweet: extract_link(tweet))

print(tweets)
# output files into csv && json
tweets.to_csv("./parse_data1.csv", index=False)
tweets.to_json("./parse_data1.json")