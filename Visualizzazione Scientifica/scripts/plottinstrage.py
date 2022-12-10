import pandas as pd
import os
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import collections

df = pd.read_csv(os.path.join(os.path.dirname(__file__),
                              "../dataset/affluenze/merged.csv"))
listPartiti = []

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

for i in dictCheck.values():
    i["centroDestra"] = round(i["centroDestra"], 2)
    i["centroSinistra"] = round(i["centroSinistra"], 2)
    i["centroPuro"] = round(i["centroPuro"], 2)
    i["altro"] = round(i["altro"], 2)

for k, v in dictCheck.items():
    v.pop("altro")

dictCheck = collections.OrderedDict(sorted(dictCheck.items()))

df = pd.DataFrame(dictCheck).T
df = pd.DataFrame(df).T
df = df.reset_index()
df = df.rename(columns={"index": "Schieramenti"})

blu = "#423fc9"
verde = "#63ce5e"
rosso = "#db625e"
colorScale = [blu, rosso, verde]

df_colonne = df.columns
fig = px.parallel_categories(df, dimensions=df_colonne,
                             color=[0, 1, 2], range_color=[0, 2], color_continuous_scale=colorScale,
                             title='Andamento schieramento elezioni per anno')
fig.update_traces(dimensions=[
    {"categoryorder": "category descending"}
])
fig.update_layout(coloraxis_colorbar=dict(title="legend", ticks='outside'))
fig.update_coloraxes(colorbar_tickmode='array')
fig.update_coloraxes(colorbar_ticktext=df["Schieramenti"])
fig.update_coloraxes(colorbar_tickvals=[0, 1, 2])

fig.show()