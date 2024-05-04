import unittest
from src.app import ask_llm
import openai

class TestAskLLM(unittest.TestCase):
    def test_ask_llm(self):
        query = "What is the meaning of life?"
        response = ask_llm(query)
        self.assertIsInstance(response, openai.types.chat.ChatCompletion, "Response is not a ChatCompletion instance")

if __name__ == '__main__':
    unittest.main()