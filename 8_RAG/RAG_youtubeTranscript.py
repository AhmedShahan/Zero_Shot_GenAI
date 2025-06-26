from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from  langchain_huggingface import HuggingFaceEmbeddings
from youtube_transcript_api import YouTubeTranscriptApi,TranscriptsDisabled
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

try:
    # If you don’t care which language, this returns the “best” one
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"])

    # Flatten it to plain text
    transcript = " ".join(chunk["text"] for chunk in transcript_list)
    print(transcript)

except TranscriptsDisabled:
    print("No captions available for this video.")

# get the transcript
# transcript=YouTubeTranscriptApi.get_transcript(video_id)
# print(transcript)

# All only text extract from teh result
# AllText=[]
# for info in transcript:
#     text=info['text']
#     AllText.append(text)
# print(AllText)

                                    ###  SPLIT THE CONTENT #######
from langchain_experimental.text_splitter import SemanticChunker
# text_splitter = SemanticChunker(
#     embedding, # এখানে আপনার নির্বাচিত এমবেডিং মডেল পাস করা হচ্ছে
#     breakpoint_threshold_type="gradient",
#     breakpoint_threshold_amount=1
# )
# )
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
# chunks = splitter.create_documents([transcript])
# import time 
# for doc in chunks:
#     print(doc.page_content)
#     print("*"*50)
#     time.sleep(2)
    
# print("Total Length of  the Text: ",len(AllText))
# print("Number fo Chunks: ",len(chunks))
# print("Percentage of Chunks: ",(len(AllText)/len(chunks))*100)
