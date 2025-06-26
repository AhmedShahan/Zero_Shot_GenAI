'''
pip install youtube-transcript-api
'''
from youtube_transcript_api import YouTubeTranscriptApi

# Replace with your YouTube video ID
video_id = "LNHBMFCzznE"

# Fetch transcript
transcript = YouTubeTranscriptApi.get_transcript(video_id)

# Print each line of the transcript
for entry in transcript:
    print(f"{entry['start']:.2f}s: {entry['text']}")
