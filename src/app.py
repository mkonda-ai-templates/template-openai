import os
import config, model
from openai import OpenAI

temperature=config.TEMPERATURE

llm = model.get_llm()

res = llm.chat.completions.create(
    model="gpt-4",
    messages=[{"role":"system", "content":"You are a Tibetian Monk. Always answer in cryptic sense"},
              {"role":"user", "content":"What is the meaning life?"}]
)

print(res)

