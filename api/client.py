import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGSMITH_TRACING"] = os.getenv("LANGSMITH_TRACING")

def get_openai_response(input_text):
    response = requests.post("http://0.0.0.0:8000/essay/invoke", json={"input": {"topic": input_text}})
    return response.json()['output']['content']

def get_ollama_response(input_text):
    response = requests.post("http://0.0.0.0:8000/poem/invoke", json={"input": {"topic": input_text}})
    return response.json()['output']

st.title("Langserve API Client with LLAMA2 and openAI")
input_text = st.text_input("Write an essay about")
input_text2 = st.text_input("Write a poem about")

if input_text:
    st.write(get_openai_response(input_text))

if input_text2:
    st.write(get_ollama_response(input_text2))



