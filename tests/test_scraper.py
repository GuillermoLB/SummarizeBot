import unittest
from app.scraper import scrape_article

class TestScraper(unittest.TestCase):
    def test_scrape_article(self):
        url = "https://example.com/sample-article"
        result = scrape_article(url)
        self.assertIn('title', result)
        self.assertIn('content', result)
        self.assertIsInstance(result['content'], str)

if __name__ == '__main__':
    unittest.main()
