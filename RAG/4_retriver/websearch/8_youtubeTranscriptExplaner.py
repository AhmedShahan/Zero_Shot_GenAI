'''
pip install youtube-transcript-api
'''
from youtube_transcript_api import YouTubeTranscriptApi

# Replace with your YouTube video ID
video_id = "LNHBMFCzznE"

# Fetch transcript
transcript = YouTubeTranscriptApi.get_transcript(video_id)

# print("Transcript:",transcript)

for info in transcript:
    # start = info['start']
    text = info['text']
    print(f"Text: {text}")
    # duration = info['duration']
    # print(f"Start: {start:.2f}s, Duration: {duration:.2f}s, Text: {text}")