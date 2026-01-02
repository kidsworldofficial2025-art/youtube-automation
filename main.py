import random
from gtts import gTTS
from moviepy.editor import *
import os
import json
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# ----------------------
# 1. Generate Story
# ----------------------
stories = [
    "Once upon a time, a small rabbit was scared of the dark. One day he became brave. Moral: Courage makes you strong.",
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

image = ImageClip("https://i.imgur.com/8Km9tLL.jpg") \
    .set_duration(audio.duration) \
    .resize(height=1280)

video = image.set_audio(audio)
video.write_videofile("final_video.mp4", fps=24)

# ----------------------
# 4. Upload to YouTube
# ----------------------
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

creds_data = json.loads(os.environ["YOUTUBE_CLIENT_SECRET"])

flow = InstalledAppFlow.from_client_config(creds_data, SCOPES)
credentials = flow.run_console()

youtube = build("youtube", "v3", credentials=credentials)

request = youtube.videos().insert(
    part="snippet,status",
    body={
        "snippet": {
            "title": "Kids Story | Moral Story",
            "description": "A short kids story with moral.",
            "tags": ["kids story", "bedtime story", "shorts"],
            "categoryId": "24"
        },
        "status": {
            "privacyStatus": "public"
        }
    },
    media_body=MediaFileUpload("final_video.mp4")
)

response = request.execute()
print("UPLOAD SUCCESS:", response["id"])
