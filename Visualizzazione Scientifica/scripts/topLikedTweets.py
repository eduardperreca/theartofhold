import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# read csv
liked_most = []
for i in os.listdir(os.path.join(os.path.dirname(__file__), "../tweetPolitic")):
    print(i)
    df = pd.read_csv(os.path.join(os.path.dirname(__file__),
                     "../tweetPolitic/" + i), sep=",", encoding="latin-1")
    liked_most.append({
        "user": i.split(".")[0],
        "numb": df["Likes"].max()
    })

# sort

print(liked_most)
liked_most = sorted(liked_most, key=lambda k: k['numb'], reverse=True)
# plot
plt.figure(figsize=(20, 10))
plt.bar([i["user"] for i in liked_most], [i["numb"] for i in liked_most])
plt.xticks(rotation=90)
plt.show()
