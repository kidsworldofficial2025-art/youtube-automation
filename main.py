import random
from TTS.api import TTS
from moviepy.editor import *

# ----------------------
# 1. Generate Story
# ----------------------
stories = [
    "Once upon a time, there was a small rabbit who was scared of the dark. One day he helped a friend and became brave. Moral: Courage makes you strong.",
    "A little bird wanted to fly high but was afraid. With practice, he flew across the sky. Moral: Never give up.",
    "A kind elephant helped everyone in the forest. One day they helped him back. Moral: Kindness always returns.",
    "A small fish believed in himself and crossed the ocean. Moral: Believe in yourself."
]

story = random.choice(stories)

with open("story.txt", "w") as f:
    f.write(story)

# ----------------------
# 2. Voice Generation
# ----------------------
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC")
tts.tts_to_file(text=story, file_path="voice.wav")

# ----------------------
# 3. Video Creation
# ----------------------
audio = AudioFileClip("voice.wav")

image = ImageClip("https://i.imgur.com/8Km9tLL.jpg") \
    .set_duration(audio.duration) \
    .resize(height=1280)

video = image.set_audio(audio)
video.write_videofile("final_video.mp4", fps=24)

print("Video created successfully!")
