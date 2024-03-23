import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
TEMPERATURE=os.getenv("TEMPERATURE")
MODEL=os.getenv("MODEL")
EMBEDDING_MODEL=os.getenv("EMBEDDING_MODEL")
SYSTEM_MESSAGE=os.getenv("SYSTEM_MESSAGE")