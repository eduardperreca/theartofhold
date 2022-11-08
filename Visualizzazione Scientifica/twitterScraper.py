import snscrape.modules.twitter as sntwitter
import pandas as pd
import text2emotion as te

query = "(from:CarloCalenda) since:2014-03-30 until:2022-11-08"

# Creating list to append tweet data to
tweets_list = []
for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    # print(tweet.json())
    tweets_list.append(
        [tweet.date, tweet.id, tweet.content, tweet.retweetCount, tweet.replyCount, tweet.likeCount, tweet.user.username ])

# Creating a dataframe from the tweets list above
tweets_df = pd.DataFrame(tweets_list, columns=[
                         'Datetime', 'Tweet Id', 'Text', 'Retweets', 'Replies', 'Likes', 'Username' ])

# export to csv
tweets_df.to_csv('tweetsCarletto.csv', index=False)

