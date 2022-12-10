import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd
import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

fields = ["Risposte"]
df = pd.read_csv(os.path.join(os.path.dirname(__file__),
                              "../dataset/sondaggio.csv"), usecols=fields)

stop_words = set(stopwords.words('italian'))
print(df["Risposte"])

df=df.dropna(axis=0,how='all')
print(df)

df["Risposte"] = df["Risposte"].apply(lambda x: " ".join(
    [word for word in word_tokenize(x) if word not in stop_words]))

text = df["Risposte"]
wordcloud = WordCloud(
    width=1920,
    height=1080,
    background_color='white',
    colormap = 'Reds_r',
).generate(str(text))

plt.imshow(wordcloud)
plt.axis("off")
print(f"Saving survey wordcloud")
plt.show()
plt.savefig(os.path.join(os.path.dirname(__file__),
            f"../image/survayRandom.png"))
