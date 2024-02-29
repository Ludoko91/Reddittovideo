from moviepy.editor import VideoFileClip,AudioFileClip,concatenate_videoclips
from moviepy.audio.fx.all import audio_fadein, audio_fadeout

class cut():
    def __init__(self,video_clip,ausgabe_pfad):
        self.video_path = video_clip
        self.clip_length = 60
        self.clips = []
        self.ausgabe_pfad = ausgabe_pfad
        self.videoclip = None

    def divide_video(self):
        self.videoclip = VideoFileClip(self.video_path)
        duration = self.videoclip.duration
        clips = []
        startzeitpunkt = 0

        while startzeitpunkt < duration-1:
            endzeitpunkt = min(startzeitpunkt + self.clip_length, duration)

            # Extrahiere den Clip von startzeitpunkt bis endzeitpunkt
            clip = self.videoclip.subclip(startzeitpunkt, endzeitpunkt)

            self.clips.append(clip)
            startzeitpunkt = endzeitpunkt - 1  # Überlappung der letzten Sekunde
            

    def safeclip(self):
        output_path = self.ausgabe_pfad.replace(".mp4","")
        # list
        output_path_fulllist =[]
        # Speichern Sie die resultierenden Clips ab
        for i, clip in enumerate(self.clips):
            output_path_full = output_path + str(i + 1) +'.mp4'
            clip.write_videofile(output_path_full, codec='libx264', audio_codec='aac')
            output_path_fulllist.append(output_path_full)

        # close Clips
        for clip in self.clips:
            clip.close()
        self.videoclip.close()
        return output_path_fulllist