import os
from JsontoVideo.processing import jsontovideo
from JsontoVideo.processing import videoedit	
from JsontoVideo.processing import cut_video

class Createvideo():
    def __init__(self,path) -> None:
        self.path = path
        self.audio_data = None
        self.title = None
        self.output_path = None
        self.video_path = None
        self.text_data = None
        self.temp_video_path = None

    def create_audio(self):
        test = jsontovideo.json_to_video(self.path,self.audio_data,self.title,self.output_path,self.video_path,self.text_data)
        data = test.json_to_audio() #output: audio_data,headline,output_path,video_path 
        #set varibale from output
        self.audio_data = data[0]
        self.title = data[1]
        self.output_path = data[2]
        self.video_path = data[3]
        self.text_data = data[4]
        print("audio done")
    

    def create_video(self):
        test = jsontovideo.json_to_video(self.path,self.audio_data,self.title,self.output_path,self.video_path,self.text_data)
        self.temp_video_path = test.audio_to_video()
        print("video created")
        
    
    def edit_video(self):
        i = videoedit.videotext(self.text_data,self.video_path,self.temp_video_path,self.output_path,self.audio_data)
        i.create_textblocks()
        video_infos= i.get_video_infos()
        txt_clips = i.create_text_clips(video_infos[0],video_infos[1])
        i.combine_text_Video2(video_infos[3],txt_clips)
        i.close_clips()

    def cut_video(self):
        cut = cut_video.cut(self.output_path,ausgabe_pfad=self.output_path)
        cut.divide_video()
        cut.safeclip()

    def delete_data(self):
        try:
            os.remove(self.temp_video_path)
            print(f'Datei {self.temp_video_path} erfolgreich gelöscht.')
        except OSError as e:
            print(f"Fehler beim Löschen der Datei {self.temp_video_path}: {e}")
