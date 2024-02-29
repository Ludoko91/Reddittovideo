from webtojson import crawler
from webtojson import builder

def reddit_json():
    url = "https://www.reddit.com/r/story.json"
    a = crawler.Crawler(url)
    #get json
    json_file = a.web_to_json()
    # get infos from json
    data_list = a.json_data(json_file)
    # initialize class
    i = builder.Json_builder()
    
    path_list = []
    #loop to build Json for every story
    for data in data_list:
        #get video path for stock video
        video_path = i.videorandomat()
        #get output_path
        output_path = i.output(data[0])
        #build new json      title,text,video_path,Outputpath
        path = i.build_json(data[0],data[1],video_path,output_path)
        path_list.append(path)

    return path_list
