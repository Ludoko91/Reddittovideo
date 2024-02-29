from JsontoVideo.processing import texttoaudio
from JsontoVideo.processing import audiotovideo




class json_to_video():

    def __init__(self,path,audio_data,title,output_path,video_path,text_data):
        self.path = path
        self.audio_data = audio_data
        self.title = title
        self.output_path = output_path
        self.video_path = video_path
        self.text_data = text_data
        
    
    def json_to_audio(self):
        #initate class
        audio = texttoaudio.Jsontoaudio(self.path)
        # get text from Json
        text_data = audio.json_to_text()
        # create name from headline
        headline = audio.json_to_headline()
        # create audio with text
        audio_data = audio.text_to_audio(headline,text_data)
        # get 
        output_path = audio.get_output_path()
        #get video path
        video_path = audio.get_video_path()
        return audio_data,headline,output_path,video_path,text_data

    def audio_to_video(self):
        #call class to process
        test = audiotovideo.Audio_to_video(self.video_path,self.audio_data,self.title,self.output_path)
        #load clips
        clip = test.call_clips()
        #get duration
        duration = test.check_duration(clip[0],clip[1]) #output: video Duration, audio Duration
        #equalize length of audio and video
        video_clip = test.length_equalizer(clip[0],duration[0],duration[1])
        #combined audio and video
        b = test.combinedAV(video_clip,clip[1])
        #safe clips
        path = test.saveclip(b,clip[0],clip[1],video_clip)
        #close all clips
        test.close_clips()
        return path
        

