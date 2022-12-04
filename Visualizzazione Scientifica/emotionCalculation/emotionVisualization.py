import text2emotion as te
import pandas as pd
import os
from googletrans import Translator
import threading

def getEmotion(text):
    translator = Translator()
    # Read the data
    df = pd.read_csv(text)

    # Initialize the list of emotions counters
    countTot = 0
    countHappy = 0
    countAngry = 0
    countSurprise = 0
    countSad = 0
    countFear = 0

    # Iterate on dataset and caluculate the emotion in percentage
    for index, row in df.iterrows():

        print(index, 'esimo tweet')
        replaced = text.replace('/Users/eduardoperreca/Desktop/Università/Visualizzazione Scientifica/emotionCalculation/../tweetPolitic/', '')
        replaced = replaced.replace('.csv', '')
        # Translate the tweet in english and calculate the emotion
        translated = translator.translate(row['Text'], dest='en')
        emotions = te.get_emotion(translated.text)
        print(emotions, 'in inglese', replaced)

        if emotions['Happy'] != 0 or emotions['Angry'] != 0 or emotions['Surprise'] != 0 or emotions['Sad'] != 0 or emotions['Fear'] != 0:
            countTot = countTot + 1
            countHappy = countHappy + emotions['Happy']
            countAngry = countAngry + emotions['Angry']
            countSurprise = countSurprise + emotions['Surprise']
            countSad = countSad + emotions['Sad']
            countFear = countFear + emotions['Fear']
        index = index + 1

    # Print the results
    print("su un totale di ", index, " tweet, ", countTot,
          " sono stati classificati come positivi o negativi")
    print("Happy: ", countHappy/countTot * 100, "%")
    print("Angry: ", countAngry/countTot * 100, "%")
    print("Surprise: ", countSurprise/countTot * 100, "%")
    print("Sad: ", countSad/countTot * 100, "%")
    print("Fear: ", countFear/countTot * 100, "%")

    # save the results in a csv file
    df = pd.DataFrame({'Emotion': ['Happy', 'Angry', 'Surprise', 'Sad', 'Fear'],
                          'Percentage': [countHappy/countTot * 100, countAngry/countTot * 100, countSurprise/countTot * 100, countSad/countTot * 100, countFear/countTot * 100],
                          'Tot Valid': [countTot, countTot, countTot, countTot, countTot]})
                        
    replaced = text.replace('/Users/eduardoperreca/Desktop/Università/Visualizzazione Scientifica/emotionCalculation/../tweetPolitic/', '')
    replaced = replaced.replace('.csv', '')
    replaced = replaced + "SentimentalAnalysis"

    df.to_csv(f'emotion{replaced}.csv', index=False)

listName = []
for i in os.listdir(os.path.join(os.path.dirname(__file__), "../tweetPolitic")):
    listName.append(i)

listDirectory = []
for i in listName:
    print(i)
    listDirectory.append(os.path.join(os.path.dirname(__file__), f"../tweetPolitic/{i}"))

# print(listDirectory)
for csv in listDirectory:
    t = threading.Thread(target=getEmotion, args=(csv,))
    t.start()
