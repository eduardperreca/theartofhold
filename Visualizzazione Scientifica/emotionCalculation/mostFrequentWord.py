import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd
import os
import threading

for i in os.listdir(os.path.join(os.path.dirname(__file__), "../tweetPolitic")):
    fields = ['Text']
    df = pd.read_csv(os.path.join(os.path.dirname(__file__),
                     "../tweetPolitic/" + i), usecols=fields)

    for x in df["Text"]:
        for j in x.split(" "):
            if len(j) < 5:
                df["Text"].replace(x, x.replace(j, ""), inplace=True)
    
    text = df["Text"]

    wordcloud = WordCloud(
        width=1800,
        height=3000,
        background_color='white'
    ).generate(str(text))

    plt.imshow(wordcloud)
    plt.axis("off")
    i = i.split(".")[0]
    print("Saving " + i + " wordcloud")
    plt.show()
    plt.savefig(os.path.join(os.path.dirname(__file__),
                f"../image/cameraRandom{i}.png"))
