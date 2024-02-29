from gtts import gTTS
import json
import re

class Jsontoaudio():

    def __init__(self, jsonpath):
        self.jsonpath = jsonpath

    def json_to_text(self):
        #get text from JSON
        with open(self.jsonpath, 'r', encoding='utf-8') as json_datei:
            jsondata = json.load(json_datei)
            text_json = jsondata.get('text', '')
        return text_json
    
    def json_to_headline(self):
        #get text from JSON
        with open(self.jsonpath, 'r', encoding='utf-8') as json_datei:
            jsondata = json.load(json_datei)
            head_json = jsondata.get('headline', '')
            headline_1 = re.sub(r'[^a-zA-Z0-9 ]', '', head_json.replace(':',''))
            headline = headline_1.replace(" ","")
        return headline
    
    def text_to_audio(self,headline,text_data):
        if text_data:
            # create gTTS-object with text
            tts = gTTS(text_data, lang='en',tld= 'co.in')  # 'de' for german

            # safe audio data as mp3
            audio_datei_pfad_row = 'JsontoVideo\data\caudio\ ' + headline + ".wav"
            audio_datei_pfad = audio_datei_pfad_row.replace(" ","")
            tts.save(audio_datei_pfad)
            print("audio done")
            return audio_datei_pfad
        else:
            print("error.no text found")
        
    def get_output_path(self):
        #get path from JSON
        with open(self.jsonpath, 'r', encoding='utf-8') as json_datei:
            jsondata = json.load(json_datei)
            path = jsondata.get('output_path', '')
        return path

    def get_video_path(self):
        #get path from JSON
        with open(self.jsonpath, 'r', encoding='utf-8') as json_datei:
            jsondata = json.load(json_datei)
            video_path = jsondata.get('video', '')
        return video_path
    
