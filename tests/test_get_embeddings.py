import unittest
from src.model import get_embeddings

class TestGetEmbeddings(unittest.TestCase):

    def test_get_embeddings(self):
        text = "This is a test sentence."
        embedding = get_embeddings(text)
        self.assertIsInstance(embedding, list)
        self.assertTrue(len(embedding) > 0)
        self.assertTrue(all(isinstance(x, (int, float)) for x in embedding))
        print("Test passed!")

if __name__ == '__main__':
    unittest.main()
