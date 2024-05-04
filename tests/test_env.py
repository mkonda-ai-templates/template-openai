import unittest
from dotenv import load_dotenv
import os

class TestEnvironmentVariables(unittest.TestCase):
    
    def setUp(self):
        load_dotenv()

    def test_openai_api_key(self):
        OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        self.assertIsNotNone(OPENAI_API_KEY)

    def test_temperature(self):
        TEMPERATURE = os.getenv("TEMPERATURE")
        self.assertIsNotNone(TEMPERATURE)

    def test_model(self):
        MODEL = os.getenv("MODEL")
        self.assertIsNotNone(MODEL)

    def test_embedding_model(self):
        EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")
        self.assertIsNotNone(EMBEDDING_MODEL)

    def test_system_message(self):
        SYSTEM_MESSAGE = os.getenv("SYSTEM_MESSAGE")
        self.assertIsNotNone(SYSTEM_MESSAGE)

if __name__ == '__main__':
    unittest.main()
