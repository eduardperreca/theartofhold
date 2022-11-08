import text2emotion as te
import pandas as pd

# Read the data
df = pd.read_csv('tweetsRenzi.csv')

# Initialize the list of emotions counters
countTot = 0
countHappy = 0
countAngry = 0
countSurprise = 0
countSad = 0
countFear = 0

# Iterate on dataset and caluculate the emotion in percentage
for index, row in df.iterrows():
    
    if index == 5000:
        break

    print(index, 'esimo tweet')

    emotions = te.get_emotion(row['Text'])
    # print(emotions)
    if emotions['Happy'] != 0 or emotions['Angry'] != 0 or emotions['Surprise'] != 0 or emotions['Sad'] != 0 or emotions['Fear'] != 0:
        countTot = countTot + 1
        countHappy = countHappy + emotions['Happy']
        countAngry = countAngry + emotions['Angry']
        countSurprise = countSurprise + emotions['Surprise']
        countSad = countSad + emotions['Sad']
        countFear = countFear + emotions['Fear']
    index = index + 1

# Print the results
print("su un totale di ", index, " tweet, ", countTot, " sono stati classificati come positivi o negativi")
print("Happy: ", countHappy/countTot * 100, "%")
print("Angry: ", countAngry/countTot * 100, "%")
print("Surprise: ", countSurprise/countTot * 100, "%")
print("Sad: ", countSad/countTot * 100, "%")
print("Fear: ", countFear/countTot * 100, "%")

