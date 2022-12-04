import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd
import os
import threading

for i in os.listdir(os.path.join(os.path.dirname(__file__), "../tweetPolitic")):
    fields = ['Text']
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), "../tweetPolitic/" + i), usecols=fields)

    text = df['Text'].values

    wordcloud = WordCloud().generate(str(text))

    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
    plt.savefig(os.path.join(os.path.dirname(__file__), f"../image/cameraRandom{i}.png"))

# listName = []
# for i in os.listdir(os.path.join(os.path.dirname(__file__), "../tweetPolitic")):
#     listName.append(i)

# listDirectory = []
# for i in listName:
#     print(i)
#     listDirectory.append(os.path.join(os.path.dirname(__file__), f"../tweetPolitic/{i}"))
    
# for i in listDirectory:
#     t = threading.Thread(target=mostFrequentWord, args=(i,))
#     t.start()