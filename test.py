from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

# Video laden
video_clip = VideoFileClip("JsontoVideo\data\Video\stock1.mp4")

# Liste von TextClips erstellen
text_clips = []
text_clips.append(TextClip("Text 1", fontsize=50, color='white').set_position(("center", "top")).set_duration(5))
text_clips.append(TextClip("Text 2", fontsize=50, color='white').set_position(("center", "bottom")).set_duration(5))

# Alle TextClips in einem CompositeVideoClip kombinieren
text_clip_combined = CompositeVideoClip(text_clips)

# TextClip über das Video legen
final_clip = CompositeVideoClip([video_clip, text_clip_combined])

# Das Video anzeigen oder speichern
final_clip.write_videofile("output.mp4")
