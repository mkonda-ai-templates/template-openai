import unittest
from src.model import get_llm

class TestGetLLM(unittest.TestCase):

    def test_get_llm(self):
        llm = get_llm()
        self.assertIsNotNone(llm)
        self.assertTrue(hasattr(llm, "chat"))
        self.assertTrue(hasattr(llm, "embeddings"))
        print("Test passed!")

if __name__ == '__main__':
    unittest.main()
