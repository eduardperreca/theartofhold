import matplotlib.pyplot as plt
import pandas as pd
import os
from scipy.interpolate import interp1d
import numpy as np

dfCurr = pd.read_csv(os.path.join(os.path.dirname(__file__), "../dataset/camera/camera_italia-20080413.txt"), sep=";", encoding="latin-1")

print(dfCurr["LISTA"].unique())