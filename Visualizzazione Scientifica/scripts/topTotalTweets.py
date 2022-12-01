import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# read csv
listOutput = []
for i in os.listdir(os.path.join(os.path.dirname(__file__), "../tweetPolitic")):
    print(i)
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), "../tweetPolitic/" + i), sep=",", encoding="latin-1")
    x, y = df.shape
    listOutput.append({
        "user": i.split(".")[0],
        "numb": x
    })

# sort
listOutput = sorted(listOutput, key=lambda k: k['numb'], reverse=True)

# plot
plt.figure(figsize=(20, 10))
plt.bar([i["user"] for i in listOutput], [i["numb"] for i in listOutput])
plt.xticks(rotation=90)
plt.show()
