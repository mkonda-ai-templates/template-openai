import os
import config
import openai
from openai import OpenAI

OPENAI_API_KEY = config.OPENAI_API_KEY
TEMPERATURE = config.TEMPERATURE
EMBEDDING_MODEL=config.EMBEDDING_MODEL
MODEL = config.MODEL

def get_llm():
    llm = OpenAI()

    return llm

def get_embeddings(text):
   text = text.replace("\n", " ")

   llm = get_llm()
   
   return llm.embeddings.create(input = [text], model=EMBEDDING_MODEL).data[0].embedding
