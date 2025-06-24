from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from  langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
load_dotenv()
MessageExplain=[
    ('system','You are helpful Ai Assistent for explaining Youtube Transcript. Explain In Brif.'),
    ('human','Explain All the things of teh video. Explain In details interm of Beginer friendly to advance. Make sure  all the things are included of the content. {content}')
]


prompt=ChatPromptTemplate.from_messages(MessageExplain)
model=ChatGoogleGenerativeAI(
    model='gemini-1.5-flash',
    temperature=0.9
)

response=StrOutputParser()
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/average_word_embeddings_levy_dependency")

                                        ###  LOAD THE YOUTUBE TRANSCRIPTS #######
# load the url
youtube_url="https://www.youtube.com/watch?v=o6vbe5G7xNo"

# Geet the video id from the url.  Usually video id is after v=...
video_id=youtube_url.split("v=")[-1]

# get the transcript
from youtube_transcript_api import YouTubeTranscriptApi
transcript=YouTubeTranscriptApi.get_transcript(video_id)
print(transcript)

# All only text extract from teh result
AllText=[]
for info in transcript:
    text=info['text']
    AllText.append(text)
print(AllText)

                                    ###  SPLIT THE CONTENT #######
from langchain_experimental.text_splitter import SemanticChunker
text_splitter = SemanticChunker(
    embedding, # এখানে আপনার নির্বাচিত এমবেডিং মডেল পাস করা হচ্ছে
    breakpoint_threshold_type="gradient",
    breakpoint_threshold_amount=1
)

chunks=text_splitter.create_documents(AllText)
print("Total Length of  the Text: ",len(AllText))
print("Number fo Chunks: ",len(chunks))
print("Percentage of Chunks: ",(len(AllText)/len(chunks))*100)
