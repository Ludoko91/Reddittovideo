import random
import string
import json
import os
import re

class Json_builder():
    
    def build_json(self,headline,text,video_path,output_path):

        data = {
            "headline"  : headline,
            "text"      : text,
            "video"     : video_path,
            "output_path": output_path
        }
        # define filepath
        folder_path = "JsontoVideo\data\JSON"
        headline_1 = re.sub(r'[^a-zA-Z0-9 ]', '', headline.replace(':',''))
        headline_c = headline_1.replace(" ","")
        file_name = headline_c + ".json"
        # create full path
        file_path = os.path.join(folder_path, file_name)
        # safe dictinary as json
        with open(file_path, 'w') as file:
            json.dump(data, file)

        return file_path
        
    def videorandomat(self):
        #get number for stock video
        number = random.randint(1,4)
        #create path
        video_path = "JsontoVideo\data\Video\stock" + str(number) + ".MP4"
        return video_path

    def output(self,title):
        headline_1 = re.sub(r'[^a-zA-Z0-9 ]', '', title.replace(':',''))
        headline_c = headline_1.replace(" ","")
        path = "JsontoVideo\data\product_video\w" + headline_c + ".mp4"
        return path


