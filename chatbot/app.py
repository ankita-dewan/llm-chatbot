from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama


import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")
os.environ["LANGSMITH_TRACING"] = os.getenv("LANGSMITH_TRACING")


# Create chatbot
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that can answer questions and help with tasks."),
    ("user", "Question: {question}"),
])

# Streamlit app
st.title("Chatbot demo with Llama 3.2")
input_text = st.text_input("Search the topic you want to know about")

# Open AI llm call
llm = Ollama(model="llama3.2")
output_parser = StrOutputParser()

#chain
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))
    
    
