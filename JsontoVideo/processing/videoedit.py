import moviepy.editor as mp
from moviepy.editor import VideoFileClip, TextClip, concatenate_videoclips
import requests

class videotext():

    def __init__(self,text,video_path,temp_video_path,output_path,audio_path):
        self.text = text
        self.video_path = video_path
        self.temp_video_path = temp_video_path
        self.output_path = output_path
        self.cliplist =  []
        self.video_duration = None
        self.text_blocks = []
        self.text_duration = []
        self.audio_path = audio_path

    def get_duration(self):
        #create list of duration for every word with lib and audio
        with open(self.text, 'r') as f:
            transcript = f.read()
        # Konfigurieren Sie die Anfrageparameter
        data = {
            'audio': open(self.audio_path, 'rb'),
            'transcript': transcript
        }
        # Senden Sie die HTTP-Anfrage an den Gentle-Server
        response = requests.post('http://localhost:8765/transcriptions', files=data)

        # Extrahieren Sie das Ergebnis aus der Antwort
        result = response.json()
        print(result)

        
   
    def create_textblocks(self):
        words_per_block = 2
        words = self.text.split()
        text_block = [words[i:i+words_per_block] for i in range(0, len(words), words_per_block)]
        self.text_blocks = [" ".join(block) for block in text_block]
    
    def get_video_infos(self):
        my_video = mp.VideoFileClip(self.temp_video_path)
        print(my_video.duration)
        w,h = moviesize = my_video.size
        duration_video = my_video.duration
        self.video_duration = duration_video
        self.cliplist.append(my_video)
        return w,h,duration_video,my_video
    
    def create_text_clips(self,w,h):
        i = 0
        duration = len(self.text_blocks)/self.video_duration
        txt_clips = []
        for text in self.text_blocks:
            txt_clip = mp.TextClip(text,font="Amiri-regular", color="white", fontsize=50) #set text properties
            txt_clip = txt_clip.set_start(i)
            txt_col = txt_clip.on_color(size=(w + txt_clip.w, txt_clip.h+5), color=(0,0,0), pos=(6,"center"), col_opacity=0.5)
            txt_clip = txt_clip.set_position("center","center").set_duration(duration)
            txt_clips.append(txt_clip)
            self.cliplist.append(txt_clip) 
            i = i + 2
        return txt_clips

    def combine_text_clips(self,txt_clips,w,h):
        #add textclip together
        final_text_clip = TextClip(".", fontsize=50, color='white', bg_color='black', size=(1920, 1080)).set_duration(0.1)
        for txt_clip in txt_clips:
            final_text_clip = concatenate_videoclips([final_text_clip,txt_clip])
            # txt in list close later
        self.cliplist.append(final_text_clip)
        return final_text_clip

    def combine_text_Video(self,my_video,txt_clips):
        # combined video and text
        final_video = mp.CompositeVideoClip([my_video,txt_clips.set_end(3)])
        final_video.write_videofile(self.output_path, fps=24, codec='libx264', audio_codec='aac')
        self.cliplist.append(final_video)

    def combine_text_Video2(self,my_video,txt_clips):
        txt_clip_final = concatenate_videoclips(txt_clips)
        txt_clip_final = txt_clip_final.set_position("center","center")
        # combined video and text
        final_video = mp.CompositeVideoClip([my_video,txt_clip_final])
        final_video.write_videofile(self.output_path, fps=24, codec='libx264', audio_codec='aac')
        self.cliplist.append(final_video)
        self.cliplist.append(txt_clip_final)

    
    def close_clips(self):
        #close clips
        for i in self.cliplist:
            i.close()
        


i = videotext(text="JsontoVideo\data\JSON\PartnerDiscordrnofriends.json",video_path=None,temp_video_path=None,output_path=None,audio_path="JsontoVideo\data\caudio\PartnerDiscordrnofriends.wav")
i.get_duration()