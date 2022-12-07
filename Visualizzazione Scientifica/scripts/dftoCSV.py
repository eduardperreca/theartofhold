import matplotlib.pyplot as plt
import pandas as pd
import os
from scipy.interpolate import interp1d
import numpy as np

# merge csv
for i in os.listdir(os.path.join(os.path.dirname(__file__), "../dataset/camera")):
    df = pd.read_csv(os.path.join(os.path.dirname(__file__),
                 "../dataset/camera/" + i ), encoding='latin-1', sep=";")

    # sort array by votes
    df = df.sort_values(by=['VOTI_LISTA'], ascending=False)

    df.to_csv(os.path.join(os.path.dirname(__file__),
                        f"../dataset/camera_sorted/{i}Output.csv"))
