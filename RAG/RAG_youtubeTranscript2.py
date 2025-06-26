                                        ###  LOAD THE YOUTUBE TRANSCRIPTS #######
# load the url
youtube_url="https://www.youtube.com/watch?v=o6vbe5G7xNo"
video_id=youtube_url.split("v=")[-1]
from youtube_transcript_api import YouTubeTranscriptApi,TranscriptsDisabled

# content=YouTubeTranscriptApi.get_transcript(video_id)
# print(content[:300])

try:
    transcript=YouTubeTranscriptApi.get_transcript(video_id)
    transcript=" ".join(chunk['text'] for chunk in transcript)
except TranscriptsDisabled:
    print("No Caption  is provided in the video")