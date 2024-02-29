from webtojson import main as webmain
from JsontoVideo.processing import main as videomain


class runclass(videomain.Createvideo):
    def __init__(self,path) -> None:
        super().__init__(path)
    def alles(self):
        path_list = webmain.reddit_json() # output: json
        for jsonpath in path_list:
            #json to video
            video = videomain.Createvideo(path=jsonpath)
            video.create_audio() 
            video.create_video()
            video.edit_video()
            video.cut_video()
            video.delete_data()
            print("video done")

