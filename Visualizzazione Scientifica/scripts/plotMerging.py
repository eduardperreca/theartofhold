import matplotlib.pyplot as plt
import pandas as pd
import os
from scipy.interpolate import interp1d
import numpy as np

df = pd.read_csv(os.path.join(os.path.dirname(__file__),
                              "../dataset/affluenze/merged.csv"))

centroDestra = ["FRATELLI D'ITALIA CON GIORGIA MELONI", "LEGA PER SALVINI PREMIER", "FORZA ITALIA","IL POPOLO DELLA LIBERTA'",
                "ITALEXIT PER L'ITALIA", "FORZA NUOVA","LEGA", "CASAPOUND ITALIA", "FRATELLI D'ITALIA", "LEGA NORD", "ALLEANZA NAZIONALE", "LEGA LOMBARDA", "MSI-DN", "P.LIBERALE ITALIANO"]

centroSinistra = ["PARTITO DEMOCRATICO - ITALIA DEMOCRATICA E PROGRESSISTA", "MOVIMENTO 5 STELLE", "+EUROPA", "ALLEANZA VERDI E SINISTRA",
                  "PARTITO DEMOCRATICO", "LIBERI E UGUALI", "MOVIMENTO 5 STELLE BEPPEGRILLO.IT", "SINISTRA ECOLOGIA LIBERTA", "L'ULIVO",
                  "DEMOCRATICI SINISTRA",  "PDS", "P.POPOLARE ITALIANO", "PSI", "PCI", "FR.DEMOCR.POPOLARE", "UNIONE DEMOCRATICA PER I CONSUMATORI"]

centroPuro = ["AZIONE - ITALIA VIVA - CALENDA",
              "SCELTA CIVICA CON MONTI PER L'ITALIA", "UNIONE DI CENTRO", "LA MARGHERITA", "DC"]


dictCheck = {}

for i in df["LISTA"].unique():
    if i in centroDestra:
        dictCheck[i] = "centroDestra"
    elif i in centroSinistra:
        dictCheck[i] = "centroSinistra"
    elif i in centroPuro:
        dictCheck[i] = "centroPuro"
    else:
        dictCheck[i] = "altro"

df["check"] = df["LISTA"].map(dictCheck)

dictCheck = {}
for i, row in df.iterrows():
    dictCheck[row["year"]] = {
        "centroDestra": 0,
        "centroSinistra": 0,
        "centroPuro": 0,
        "altro": 0,
    }

for i, row in df.iterrows():
    dictCheck[row["year"]][row["check"]] += row["PERCENTUALE"]

for key, value in dictCheck.items():
    print(key, value)

dictCheck = dict(sorted(dictCheck.items()))

y = np.array([dictCheck[i]["centroDestra"] for i in dictCheck.keys()])
x = np.array([i for i in dictCheck.keys()])
cubic_interpolation_model = interp1d(x, y, kind="cubic")
x_ = np.linspace(x.min(), x.max(), 200)
y_ = cubic_interpolation_model(x_)
plt.plot(x_, y_, color="b")

y2 = np.array([dictCheck[i]["centroSinistra"] for i in dictCheck.keys()])
x2 = np.array([i for i in dictCheck.keys()])
cubic_interpolation_model = interp1d(x2, y2, kind="cubic")
x2_ = np.linspace(x2.min(), x2.max(), 00)
y2_ = cubic_interpolation_model(x2_)
plt.plot(x2_, y2_, color="g")

y3 = np.array([dictCheck[i]["centroPuro"] for i in dictCheck.keys()])
x3 = np.array([i for i in dictCheck.keys()])
cubic_interpolation_model = interp1d(x3, y3, kind="cubic")
x3_ = np.linspace(x3.min(), x3.max(), 200)
y3_ = cubic_interpolation_model(x3_)
plt.plot(x3_, y3_, color="r")

y4 = np.array([dictCheck[i]["centroSinistra"] for i in dictCheck.keys()])
x4 = np.array([i for i in dictCheck.keys()])
cubic_interpolation_model = interp1d(x4, y4, kind="cubic")
x4_ = np.linspace(x4.min(), x4.max(), 200)
y4_ = cubic_interpolation_model(x4_)
plt.plot(x4_, y4_, color="y")

y5 = np.array([dictCheck[i]["altro"] for i in dictCheck.keys()])
x5 = np.array([i for i in dictCheck.keys()])
cubic_interpolation_model = interp1d(x5, y5, kind="cubic")
x5_ = np.linspace(x5.min(), x5.max(), 200)
y5_ = cubic_interpolation_model(x5_)
plt.plot(x5_, y5_, color="c")

plt.legend(["Centro Destra", "Centro Puro", "Centro Sinistra", "wtf"])

plt.show()