import unittest
from src.worker import compress_image

class TestWorker(unittest.TestCase):
    def test_compress_image(self):
        url = 'https://example.com/test.jpg'
        output = compress_image(url)
        self.assertIsNotNone(output)
        self.assertLess(output.tell(), 500000)  # Assuming < 500KB

if __name__ == '__main__':
    unittest.main()
