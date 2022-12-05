import matplotlib.pyplot as plt
import pandas as pd
import os
from scipy.interpolate import interp1d
import numpy as np

for i in os.listdir(os.path.join(os.path.dirname(__file__), "../emotionCalculation/calculation")):
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), "../emotionCalculation/calculation/" + i), sep=",", encoding="latin-1")
    # lista = df["Percentage"].values
    # print(lista)
    y = np.array(df["Percentage"])
    
    plt.pie(y, labels=df["Emotion"], autopct='%1.1f%%')
    plt.title("Emotion of " + i.split(".")[0])
    plt.show()
    plt.savefig(os.path.join(os.path.dirname(__file__), "../image/" + i.split(".")[0] + ".png"))
