'''
pip install youtube-transcript-api
'''
from youtube_transcript_api import YouTubeTranscriptApi
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
# Replace with your YouTube video ID
video_id = "LNHBMFCzznE"

# Fetch transcript
transcript = YouTubeTranscriptApi.get_transcript(video_id)

# print("Transcript:",transcript)
AllText=[]
for info in transcript:
    # start = info['start']
    text = info['text']
    # print(f"Text: {text}")
    AllText.append(text)
    # duration = info['duration']
    # print(f"Start: {start:.2f}s, Duration: {duration:.2f}s, Text: {text}")

MessageExplain=[
    ('system', 'You are a helpful assistant that explains YouTube video transcripts. Please Explain in Native English Language.'),
    ('human','Explain the following YouTube video transcript in English:{ytText}')
]


prompt=ChatPromptTemplate.from_messages(MessageExplain)
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                             temperature=0.1)
parser=StrOutputParser()
chain=prompt | llm | parser

response= chain.invoke({
    "ytText": AllText
})

print(response)