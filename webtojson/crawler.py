import json
import requests

class Crawler():
    def __init__(self,url) -> None:
        self.url = url

    def web_to_json(self):

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
        }

        # request json via url
        response = requests.get(self.url, headers=headers)

        json_object = response.json()
        return json_object
    
    def json_data(self,json_data):
        
        children_number = 0
        data_found = []
        while True:
            try:
                #get title and text from json
                title = json_data['data']['children'][children_number]['data']['title']
                text = json_data['data']['children'][children_number]['data']['selftext']
                data_found.append([title,text])
                children_number = children_number + 1
            except IndexError:
                break
        return data_found
    
        





