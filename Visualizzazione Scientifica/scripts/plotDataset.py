import matplotlib.pyplot as plt
import pandas as pd
import os

# read csv
df = pd.read_csv(os.path.join(os.path.dirname(__file__),
                              "../dataset/referendum/referendum2022.csv"), sep=';', encoding='latin-1')

totElett = 0
totVotanti = 0

# list of regions
regions = df['REGIONE'].unique()

dictRegion = {}

for region in regions:
    dfRegion = df[df['REGIONE'] == region]
    totVotanti = dfRegion['VOTANTI_TERZA'].sum()
    totElett = dfRegion['ELETTORI'].sum()
    percVotanti = totVotanti / totElett * 100
    dictRegion[region] = {'totElett': totElett,
                          'totVotanti': totVotanti, 'percVotanti': percVotanti.round()}

x = []
y = []
y2 = []

for region in dictRegion:
    x.append(region)
    y.append(dictRegion[region]['totVotanti'])
    y2.append(dictRegion[region]['totElett'])

plt.bar(x, y, color='r')
plt.bar(x, y2, bottom=y, color='b')
plt.show()
