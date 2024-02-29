from moviepy.editor import VideoFileClip,AudioFileClip,concatenate_videoclips
from moviepy.audio.fx.all import audio_fadein, audio_fadeout


class Audio_to_video():
    def __init__(self,video_pfad,audio_pfad,headline,ausgabe_pfad = None):
        self.video_pfad = video_pfad
        self.audio_pfad = audio_pfad
        self.ausgabe_pfad = ausgabe_pfad
        self.headline = headline
        self.close_list = []

    def call_clips(self):
        # load audio and video file
        video_clip_row = VideoFileClip(self.video_pfad)
        audio_clip = AudioFileClip(self.audio_pfad)
        self.close_list.append(video_clip_row)
        self.close_list.append(audio_clip)
        return video_clip_row,audio_clip
    
    def check_duration(self,video_clip,audio_clip):
        # get video duration
        video_duration = video_clip.duration
        audio_duration = audio_clip.duration
        return video_duration,audio_duration
    
    def repeat_video(self,length,video_clip_row,video_duration):
        # calculate how  many times to repeat clip
        repeation = int(length / video_duration) + 1
        # create list of reapeated clip
        repeated_clips = [video_clip_row] * repeation
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # connect clips
        complet_clip = concatenate_videoclips(repeated_clips, method="compose")
        # cut clip to needed length
        gesamter_clip = complet_clip.subclip(0, length) #complet clip need closing
        self.close_list.append(gesamter_clip)
        return gesamter_clip
    
    def length_equalizer(self,video_clip,video_duration,audio_duration):
        # check if video or audio is longer
        if video_duration >= audio_duration:
            #cut video to audio length
            video_clip_rdy = video_clip.set_end(audio_duration)
            self.close_list.append(video_clip_rdy)
            self.close_list.append(video_clip)
            return video_clip_rdy
        elif video_duration <= audio_duration:
            #repeat video till audio length is reached
            video_clip_rdy = Audio_to_video.repeat_video(self,audio_duration,video_clip,video_duration)
            self.close_list.append(video_clip_rdy)
            self.close_list.append(video_clip)
            return	video_clip_rdy
        else:
            print("error length")

    def combinedAV(self,video_clip_row,audio_clip):
        # extract audio from clip
        video_clip = video_clip_row.set_audio(audio_clip)
        self.close_list.append(audio_clip)
        return video_clip

    def saveclip(self,clip,original_clip,audio_clip,video_clip):
        #edit output path
        output_path_full = self.ausgabe_pfad.replace(".mp4", "tempfull.mp4")
        #save clip
        clip.write_videofile(output_path_full, codec='libx264', audio_codec='aac')
        self.close_list.append(clip)
        return output_path_full

    def close_clips(self):
        for i in self.close_list:
            i.close()
        


