from gtts import gTTS
import json
import re

jsonpath = "test.json"

def json_to_text(jsonpath):
        #get text from JSON
        with open(jsonpath, 'r', encoding='utf-8') as json_datei:
            jsondata = json.load(json_datei)
            text_json = jsondata.get('text', '')
        return text_json
    
def json_to_headline(jsonpath):
    #get text from JSON
    with open(jsonpath, 'r', encoding='utf-8') as json_datei:
        jsondata = json.load(json_datei)
        head_json = jsondata.get('headline', '')
        headline_1 = re.sub(r'[^a-zA-Z0-9 ]', '', head_json.replace(':',''))
        headline = headline_1.replace(" ","")
    return headline

def text_to_audio(headline,text_data):
        if text_data:
            # create gTTS-object with text
            tts = gTTS(text_data, lang='en',tld= 'co.in',slow= False)  # 'de' for german

            # safe audio data as mp3
            audio_datei_pfad_row = 'JsontoVideo\data\caudio\s_test' + ".wav"
            audio_datei_pfad = audio_datei_pfad_row.replace(" ","")
            tts.save(audio_datei_pfad)
            print("done")
            return audio_datei_pfad
        else:
            print("error.no text found")


text = json_to_text(jsonpath)
headline = json_to_headline(jsonpath)
text_to_audio(headline,text)