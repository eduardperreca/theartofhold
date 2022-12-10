import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd
import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

for i in os.listdir(os.path.join(os.path.dirname(__file__), "../tweetPolitic")):
    fields = ['Text']
    df = pd.read_csv(os.path.join(os.path.dirname(__file__),
                                "../tweetPolitic/" + i), usecols=fields)

    stop_words = set(stopwords.words('italian'))

    df["Text"] = df["Text"].apply(lambda x: " ".join([word for word in word_tokenize(x) if word not in stop_words]))

    text = df["Text"]
    wordcloud = WordCloud(
        width=1080,
        height=1920,
        background_color='white',
        colormap = 'Reds',
    ).generate(str(text))

    plt.imshow(wordcloud)
    plt.axis("off")
    print(f"Saving {i} wordcloud")
    plt.show()
    plt.savefig(os.path.join(os.path.dirname(__file__),
                f"../image/camera{i}Random.png"))
