import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# read csv
interactions_sum = []
for i in os.listdir(os.path.join(os.path.dirname(__file__), "../tweetPolitic")):
    print(i)
    df = pd.read_csv(os.path.join(os.path.dirname(__file__),
                     "../tweetPolitic/" + i), sep=",", encoding="latin-1")
    interactions_sum.append({
        "user": i.split(".")[0],
        "likes": df["Likes"].sum(),
        "retweets": df["Retweets"].sum(),
        "replies": df["Replies"].sum()
    })

# sort

print(interactions_sum)
interactions_sum = sorted(interactions_sum, key=lambda k: k['likes'], reverse=True)
# plot

plot_data = {
    "user": [i["user"] for i in interactions_sum],
    "likes": [i["likes"] for i in interactions_sum],
    "retweets": [i["retweets"] for i in interactions_sum],
    "replies": [i["replies"] for i in interactions_sum]
}

df = pd.DataFrame(plot_data)
df.plot(x="user", y=["likes", "retweets", "replies"], kind="bar", figsize=(20, 10))
plt.xticks(rotation=90)
plt.show()

# plt.figure(figsize=(20, 10))
# plt.bar([i["user"] for i in interactions_sum], [i["likes"] for i in interactions_sum])
# plt.bar([i["user"] for i in interactions_sum], [i["replies"] for i in interactions_sum])
# plt.bar([i["user"] for i in interactions_sum], [i["retweets"] for i in interactions_sum])
# plt.xticks(rotation=90)
# plt.show()
