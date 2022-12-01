import matplotlib.pyplot as plt
import pandas as pd
import os
from scipy.interpolate import interp1d
import numpy as np


import matplotlib.pyplot as plt
import pandas as pd
import os
from scipy.interpolate import interp1d
import numpy as np

# read csv
dictYears = {}

# merge csv
for i in os.listdir(os.path.join(os.path.dirname(__file__), "../dataset/camera")):

    year = i.split("-")[1].split(".")[0]
    year = int(year[:4]) 
    dfCurr = pd.read_csv(os.path.join(os.path.dirname(__file__), "../dataset/camera/" + i), sep=";", encoding="latin-1")
    dfCurr["year"] = year
    dfCurr = dfCurr[["year", "LISTA", "VOTI_LISTA"]]
    dfCurr = dfCurr.groupby(["year", "LISTA"]).sum().reset_index()
    dictYears[year] = dfCurr


print(dictYears)
df = pd.concat(dictYears.values(), ignore_index=True)
df = df.groupby(["year", "LISTA"]).sum().reset_index()
df = df.sort_values(by=["year", "VOTI_LISTA"], ascending=False)
df.to_csv(os.path.join(os.path.dirname(__file__), "../dataset/camera/merged.csv"), index=False)