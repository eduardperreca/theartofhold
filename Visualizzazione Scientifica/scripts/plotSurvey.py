import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# read csv
dictReplies = {}

df = pd.read_csv(os.path.join(os.path.dirname(__file__),
                 "../dataset/sondaggio.csv"), sep=",", encoding="latin-1")

df = df[["Ti senti rappresentato dalla Politica attuale?"]]
for i in df["Ti senti rappresentato dalla Politica attuale?"]:
    if i in dictReplies.keys():
        dictReplies[i] += 1
    else:
        dictReplies[i] = 1

y = np.array([dictReplies[i] for i in dictReplies.keys()])

plt.pie(y, autopct='%1.1f%%')
plt.title("Rappresentatività della politica attuale")
plt.legend(dictReplies.keys(), loc="best")
plt.show()