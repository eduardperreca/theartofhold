import matplotlib.pyplot as plt
import pandas as pd
import os
from scipy.interpolate import interp1d
import numpy as np

df = pd.read_csv(os.path.join(os.path.dirname(__file__),
                              "../dataset/affluenze/merged.csv"))

centroDestra = ["FRATELLI D'ITALIA CON GIORGIA MELONI", "LEGA PER SALVINI PREMIER", "FORZA ITALIA",
                "ITALEXIT PER L'ITALIA", "LEGA", "CASAPOUND ITALIA", "FRATELLI D'ITALIA", "LEGA NORD", "ALLEANZA NAZIONALE", "LEGA LOMBARDA", "MSI-DN"]

centroSinistra = ["PARTITO DEMOCRATICO - ITALIA DEMOCRATICA E PROGRESSISTA", "MOVIMENTO 5 STELLE", "+EUROPA", "ALLEANZA VERDI E SINISTRA",
                  "PARTITO DEMOCRATICO", "LIBERI E UGUALI", "MOVIMENTO 5 STELLE BEPPEGRILLO.IT", "IL POPOLO DELLA LIBERTA'", "SINISTRA ECOLOGIA LIBERTA", "L'ULIVO",
                  "DEMOCRATICI SINISTRA",  "PDS", "P.POPOLARE ITALIANO", "PSI", "PCI", "FR.DEMOCR.POPOLARE"]

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
