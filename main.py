import random
from gtts import gTTS
from moviepy.editor import ImageClip, AudioFileClip
import os

# ----------------------
# 1. Generate Story
# ----------------------
stories = [
    "Once upon a time, a small rabbit was afraid of the dark. One day he became brave. Moral: Courage makes you strong.",
    "A little bird wanted to fly high but was afraid. One day it tried and succeeded. Moral: Never give up.",
    "A kind elephant helped everyone and one day they helped him back. Moral: Kindness always returns."
]

story = random.choice(stories)

with open("story.txt", "w") as f:
    f.write(story)

# ----------------------
# 2. Voice Generation
# ----------------------
tts = gTTS(text=story, lang="en")
tts.save("voice.mp3")

# ----------------------
# 3. Create Video
# ----------------------
audio = AudioFileClip("voice.mp3")

image = ImageClip("background.jpg")
image = image.set_duration(audio.duration)
image = image.resize(height=1280)

video = image.set_audio(audio)
video.write_videofile("final_video.mp4", fps=24)

print("✅ Video created successfully!")
