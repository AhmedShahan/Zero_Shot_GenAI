from youtube_transcript_api import YouTubeTranscriptApi
from langchain_google_genai import  ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from  langchain.prompts import  ChatPromptTemplate
import streamlit as st


youtubeLink=st.chat_input("Enter you  youtube link")



# print("Transcript:",transcript)





def get_text(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    AllText=[]
    for info in transcript:
        # start = info['start']
        text = info['text']
        # print(f"Text: {text}")
        AllText.append(text)
        # duration = info['duration']
        # print(f"Start: {start:.2f}s, Duration: {duration:.2f}s, Text: {text}")

    MessageExplain=[
        ('system', 'You are a helpful assistant that explains YouTube video transcripts. Please Explain in Native Bangla Language.'),
        ('human','Explain the following YouTube video transcript in Bangla:{ytText}')
    ]


    prompt=ChatPromptTemplate.from_messages(MessageExplain)
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                                temperature=0.1)
    parser=StrOutputParser()
    chain=prompt | llm | parser

    result=chain.stream({
        "ytText": AllText
    })

    return result




if youtubeLink:
    try:
        video_id = youtubeLink.split("v=")[-1]
    except:
        print("Exception")
    
    if  video_id:
        res=get_text(video_id)
        st.write(res)
    else:
        st.write("No vide id")
