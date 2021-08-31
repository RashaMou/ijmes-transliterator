from dotenv import load_dotenv
import os
import json
import requests

load_dotenv()
farasa_url = 'https://farasa.qcri.org/webapi/diacritize/'
api_key = os.getenv("FARASA_API_KEY")

text = "يُشَارُ إِلَى أَنَّ اللُّغَةَ العَرَبيَّةَ يَتَحَدَّثُها أَكْثَرُ مِنْ 422 مِلْيونَ نَسَمَةٍ وَيَتَوَزَّعُ مُتَحَدِّثُوهَا فِي المِنْطَقَةِ المَعْروفَةِ بِاسْمِ الوَطَنِ العَرَبيِّ بِالْإِضَافَةِ إِلَى العَديدِ مِنْ المَناطِقِ الأُخْرَى المُجاوِرَةِ مِثْلَ الأَهْوَازِ وَتُرْكِيَا وَتِشادَ والسِّنْغالِ وَإِريتْريا وَغَيْرِها . وَهِيَ اللُّغَةُ الرّابِعَةُ مِنْ لُغاتِ مُنَظَّمَةِ الأُمَمِ المُتَّحِدَةِ الرَّسْميَّةِ السِّتِّ ."
text2 = "this is the way to do it"

def diacritize(input):
    payload = {'text': input['text'], 'api_key': api_key}
    data = requests.post(farasa_url, data=payload)
    result = json.loads(data.text)
    print(result)
    return result

# "now we have a string"
# we want:
# [
#     {1: ["n", "o", "w"]},
#     {2: ["w", "e"]}
# ]

# split string into array
# ["now", "we", "have", "a", "string"]
# loop over the array
# for each word in the array, wordToArray(word), and stick it in a dictionary with its index as the key

def splitStringToArray(string):
    arrayOfWords = string.split()
    arrayOfLetters = []
    #[asas, asa, asas, asas]
    # loop over, and for each, push onto new array
    for word in arrayOfWords:
        # push onto new array
         arrayOfLetters.append([ch for ch in word])
    print(arrayOfLetters)
    return arrayOfLetters


splitStringToArray(text2)