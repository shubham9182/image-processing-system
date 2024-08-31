import unittest
from src.main import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_upload_api(self):
        with open('sample.csv', 'rb') as file:
            response = self.app.post('/api/upload', data={'file': file})
            self.assertEqual(response.status_code, 202)
            self.assertIn('request_id', response.json)

    def test_status_api(self):
        response = self.app.get('/api/status?request_id=some_id')
        self.assertIn(response.status_code, [200, 404])

if __name__ == '__main__':
    unittest.main()
