import matplotlib.pyplot as plt
import pandas as pd


def main():
    x = []
    y = []

    df = pd.read_csv('politicheDataset2022.csv', delimiter=',')

    print(df["COLLEGIO PLURINOMINALE"])




if __name__ == '__main__':
    main()
