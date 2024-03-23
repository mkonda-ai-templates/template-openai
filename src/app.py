import os
import config, model
from openai import OpenAI

temperature=config.TEMPERATURE
SYSTEM_MESSAGE=config.SYSTEM_MESSAGE

llm = model.get_llm()

def ask_llm(query):
    print(SYSTEM_MESSAGE)
    print(query)
    completion = llm.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role":"system", "content":SYSTEM_MESSAGE},
            {"role":"user", "content":query}
        ])
    
    return completion

res = ask_llm("What is the meaning life?")

print(res.choices[0].message.content)
