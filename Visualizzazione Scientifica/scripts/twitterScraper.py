import snscrape.modules.twitter as sntwitter
import pandas as pd
import text2emotion as te
import threading

def get_tweets(user):
    print("User: " + user)
    query = f"(from:{user}) since:2018-7-1 until:2022-11-30"

    # Creating list to append tweet data to
    tweets_list = []
    print("grabbing tweets")
    i = 0
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        # print(tweet.json())
        tweets_list.append(
            [tweet.date, tweet.id, tweet.content, tweet.retweetCount, tweet.replyCount, tweet.likeCount, tweet.user.username])
        i += 1
        print(user, i)

    # Creating a dataframe from the tweets list above
    tweets_df = pd.DataFrame(tweets_list, columns=[
        'Datetime', 'Tweet Id', 'Text', 'Retweets', 'Replies', 'Likes', 'Username'])
    print(
        f"tweets grabbed, saving to csv, please wait, 'tweets{user}.csv' will be created")
    # export to csv
    tweets_df.to_csv(f'tweets{user}.csv', index=False)


list_of_users = ["GiuseppeConteIT"]
for user in list_of_users:
    t = threading.Thread(target=get_tweets, args=(user,))
    t.start()