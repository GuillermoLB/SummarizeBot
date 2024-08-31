import unittest
from fastapi.testclient import TestClient
from app.app import app  # Import the FastAPI app instance

class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_homepage_loads(self):
        # Send a GET request to the root endpoint
        response = self.client.get("/")
        
        # Check that the status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Check that the Content-Type is HTML
        content_type = response.headers.get("content-type")
        self.assertIn("text/html", content_type)
        
        # Check that the response contains expected HTML content
        html_response = response.text
        self.assertIn("<h1>SummarizeBot</h1>", html_response)
        self.assertIn('<form id="summarizeForm">', html_response)
        self.assertIn('<label for="urlInput">Enter Article URL:</label>', html_response)
        self.assertIn('<input type="text" id="urlInput" name="url"', html_response)
        self.assertIn('<div id="summaryResult" class="result">', html_response)
        
        
    def test_summary_generation(self):
        response = self.client.post("/summarize/", json={"url": "https://example.com/sample-article"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("summary", response.json())

if __name__ == '__main__':
    unittest.main()
