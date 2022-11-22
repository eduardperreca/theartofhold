import matplotlib.pyplot as plt
import pandas as pd
import os
from scipy.interpolate import interp1d
import numpy as np

# read csv
dictYears = {}
totVotanti = 0
totElettori = 0
years = []

# merge csv
for i in os.listdir(os.path.join(os.path.dirname(__file__), "../dataset/referendum")):
    totVotanti = 0
    totElettori = 0
 
    year = i.split("-")[1].split(".")[0]
    year = int(year[:4]) 
    dfCurr = pd.read_csv(os.path.join(os.path.dirname(__file__), "../dataset/referendum/" + i), sep=";", encoding="latin-1")
    dfCurr["year"] = year
    dfCurr = dfCurr[["ELETTORI", "VOTANTI", "year"]]
    totVotanti = dfCurr["VOTANTI"].sum()
    totElettori = dfCurr["ELETTORI"].sum()
    dictYears[year] = {
        "ELETTORI": totElettori,
        "VOTANTI": totVotanti,
        "PERCENTUALE": (totVotanti / totElettori *100).round(),
        "ANNO": int(year),
    }

dictYears = dict(sorted(dictYears.items()))
y = np.array([dictYears[i]["PERCENTUALE"] for i in dictYears.keys()])
x = np.array([dictYears[i]["ANNO"] for i in dictYears.keys()])

cubic_interpolation_model = interp1d(x, y, kind = "cubic")
x_ = np.linspace(x.min(), x.max(), 300)
y_ = cubic_interpolation_model(x_)

plt.plot(x_, y_, color = "b")
plt.grid(True)
plt.title("Percentuale affluneza referendum dal 1974 al 2022")
plt.xlabel("Anno")
plt.ylabel("Affluenza (%)")
plt.savefig(os.path.join(os.path.dirname(__file__), "../image/affluenzaReferendum.png")) 