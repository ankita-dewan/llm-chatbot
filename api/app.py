from fastapi import FastAPI
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
from langserve import add_routes

import uvicorn
import os

from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

app = FastAPI(
    title="Langserve API",
    description="A simple API for Langserve",
    version="0.1.0",
)

add_routes(app, ChatOpenAI(model="gpt-4o-mini", temperature=0), path="/openai")
add_routes(app, Ollama(model="llama3.2"), path="/ollama")

prompt1 = ChatPromptTemplate.from_template("Write an essay about {topic} in 1000 words")
prompt2 = ChatPromptTemplate.from_template("Write a poem about {topic} for a 5 year old child")

add_routes(app, prompt1 | ChatOpenAI(model="gpt-4o-mini", temperature=0), path="/essay")
add_routes(app, prompt2 | Ollama(model="llama3.2"), path="/poem")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)










