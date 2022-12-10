import matplotlib.pyplot as plt
import pandas as pd
import os
from scipy.interpolate import interp1d
import numpy as np
import plotly.graph_objects as go

df = pd.read_csv(os.path.join(os.path.dirname(__file__),
                              "../dataset/affluenze/merged.csv"))
listPartiti = []

# for i in df["LISTA"].unique():
#     listPartiti.append(i)

# print(listPartiti)
centroDestra = ["BLOCCO NAZIONALE", "MSI", "SVP", "SVP - PATT",
                "Sï¿½DTIROLER VOLKSPARTEI (SVP) - PATT", 'PRI-P.RAD.', "LEGA NORD", "MSI-DN", "CENTRO CRIST.DEM.", "FORZA ITALIA", "PANNELLA-SGARBI", "LISTA PANNELLA",
                "CCD-CDU", "PANNELLA-BONINO", "IL POPOLO DELLA LIBERTA'", "MOVIMENTO PER L'AUTONOMIA ALL.PER IL SUD", "LA DESTRA - FIAMMA TRICOLORE", "FIAMMA TRICOLORE",
                "NOI CON L'ITALIA - UDC", "FRATELLI D'ITALIA CON GIORGIA MELONI", "FRATELLI D'ITALIA", "LEGA PER SALVINI PREMIER", "LEGA", "CASAPOUND ITALIA",
                "IL POPOLO DELLA FAMIGLIA", "ITALEXIT PER L'ITALIA", "ITALIA SOVRANA E POPOLARE"]

centroSinistra = ["UNITA' SOCIALISTA", "PCI", "PSI", "PCI-PSI-PDUP", "PDS", "RIFONDAZIONE COMUNISTA", "FEDERAZIONE DEI VERDI", "DEM.CRIST.-NUOVO PSI",
                  "LA RETE-MOV.DEM.", "ALLEANZA DEMOCRATICA", "POP-SVP-PRI-UD-PRODI", "RINNOVAMENTO IT-DINI", "PARTITO SOCIALISTA", "DEMOCRATICI SINISTRA",
                  "LA MARGHERITA", "IL GIRASOLE", "PARTITO DEMOCRATICO", "PARTITO DEMOCRATICO - ITALIA DEMOCRATICA E PROGRESSISTA", "DI PIETRO ITALIA DEI VALORI",
                  "MOVIMENTO 5 STELLE", "MOVIMENTO 5 STELLE BEPPEGRILLO.IT", "RIVOLUZIONE CIVILE", "SINISTRA ECOLOGIA LIBERTA'", "CENTRO DEMOCRATICO",  "IMPEGNO CIVICO LUIGI DI MAIO - CENTRO DEMOCRATICO",
                  "+EUROPA", "+EUROPA", "ITALIA EUROPA INSIEME", "CIVICA POPOLARE LORENZIN", "LIBERI E UGUALI",
                  "ALLEANZA VERDI E SINISTRA", "POTERE AL POPOLO!", "UNIONE POPOLARE CON DE MAGISTRIS", "UNIONE POP.", "LA SINISTRA L'ARCOBALENO", "L'ULIVO",
                  "DC-PCI-PSI-PSDI", "DC-UV-RV-PSDI",  "DC-PSDI-PRI", "FR.DEMOCR.POPOLARE", "PARTITO COMUNISTA ITALIANO"]

centroPuro = ["DC", "PSDI", 'PLI', 'PRI', 'PLI-PRI-PSDI',
              "UNIONE DI CENTRO", "SCELTA CIVICA CON MONTI PER L'ITALIA", "FUTURO E LIBERTA'",
              "AZIONE - ITALIA VIVA - CALENDA", "NOI MODERATI/LUPI - TOTI - BRUGNARO - UDC", "PARTITO ANIMALISTA - UCDL - 10 VOLTE MEGLIO"]

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

# for key, value in dictCheck.items():
#     print(key, value)

# dictCheck = dict(sorted(dictCheck.items()))

# y = np.array([dictCheck[i]["centroDestra"] for i in dictCheck.keys()])
# x = np.array([i for i in dictCheck.keys()])
# cubic_interpolation_model = interp1d(x, y, kind="cubic")
# x_ = np.linspace(x.min(), x.max(), 200)
# y_ = cubic_interpolation_model(x_)
# plt.plot(x_, y_, color="b")

# # y2 = np.array([dictCheck[i]["centroSinistra"] for i in dictCheck.keys()])
# # x2 = np.array([i for i in dictCheck.keys()])
# # cubic_interpolation_model = interp1d(x2, y2, kind="cubic")
# # x2_ = np.linspace(x2.min(), x2.max(), 200)
# # y2_ = cubic_interpolation_model(x2_)
# # plt.plot(x2_, y2_, color="r")

# y3 = np.array([dictCheck[i]["centroPuro"] for i in dictCheck.keys()])
# x3 = np.array([i for i in dictCheck.keys()])
# cubic_interpolation_model = interp1d(x3, y3, kind="cubic")
# x3_ = np.linspace(x3.min(), x3.max(), 200)
# y3_ = cubic_interpolation_model(x3_)
# plt.plot(x3_, y3_, color="g")

# # y5 = np.array([dictCheck[i]["altro"] for i in dictCheck.keys()])
# # x5 = np.array([i for i in dictCheck.keys()])
# # cubic_interpolation_model = interp1d(x5, y5, kind="cubic")
# # x5_ = np.linspace(x5.min(), x5.max(), 200)
# # y5_ = cubic_interpolation_model(x5_)
# # plt.plot(x5_, y5_, color="c")


# plt.title("Paragone evoluzione tra CDX e Centro Puro")
# plt.xlabel("Anno")
# plt.ylabel("Percentuale voti")
# plt.legend(["Centro Destra", "Centro Puro"])

# plt.show()
