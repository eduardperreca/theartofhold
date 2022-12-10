import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# read csv
groupedYear = {}
for i in os.listdir(os.path.join(os.path.dirname(__file__), "../tweetPolitic")):
    print(i)
    df = pd.read_csv(os.path.join(os.path.dirname(__file__),
                     "../tweetPolitic/" + i), sep=",", encoding="latin-1")

    df = pd.to_datetime(df["Datetime"]).dt.year

    df = df.value_counts().to_frame().reset_index()
    df.columns = ["Year", "Group"]
    df = df.groupby("Year").sum().reset_index()

    groupedYear[i.split(".")[0]] = df

x = groupedYear["tweetsmatteosalvinimi"]["Year"].values
print(x)

for i in groupedYear["tweetsGiuseppeConteIT"]["Group"].values:
    print(i)

ySalvini = groupedYear["tweetsmatteosalvinimi"]["Group"].values
yRenzi = groupedYear["tweetsmatteorenzi"]["Group"].values
yMeloni = groupedYear["tweetsGiorgiaMeloni"]["Group"].values
yConte = groupedYear["tweetsGiuseppeConteIT"]["Group"].values
yLetta = groupedYear["tweetsEnricoLetta"]["Group"].values
yCalenda = groupedYear["tweetsCarloCalenda"]["Group"].values

print(len(x))
print(len(ySalvini))

x_axis = np.arange(len(x))

plt.bar(x_axis - 0.3, ySalvini, 0.1, label="Salvini",)
plt.bar(x_axis - 0.2, yCalenda, 0.1, label="Calenda")
plt.bar(x_axis - 0.1, yRenzi, 0.1, label="Renzi")
plt.bar(x_axis + 0, yMeloni, 0.1, label="Meloni")
plt.bar(x_axis + 0.1, yConte, 0.1, label="Conte")
plt.bar(x_axis + 0.2, yLetta, 0.1, label="Letta")

plt.xticks(x_axis, x)
plt.xlabel("Year")
plt.ylabel("Number of Tweets")
plt.title("Number of Tweets in each year")
plt.legend()
plt.show()


# # Ygirls = [10,20,20,40]
# # Zboys = [20,30,25,30]
  
# # X_axis = np.arange(len(X))
  
# # plt.bar(X_axis - 0.2, Ygirls, 0.4, label = 'Girls')
# # plt.bar(X_axis + 0.2, Zboys, 0.4, label = 'Boys')
  
# # plt.xticks(X_axis, X)
# # plt.xlabel("Groups")
# # plt.ylabel("Number of Students")
# # plt.title("Number of Students in each group")
# # plt.legend()
# # plt.show()
