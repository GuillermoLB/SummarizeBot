import unittest
from app.scraper import scrape_article
from app.summarizer import generate_summary

class TestIntegration(unittest.TestCase):
    def test_article_summarization(self):
        url = "https://example.com/sample-article"
        article_data = scrape_article(url)
        summary = generate_summary(article_data['content'])
        self.assertTrue(len(summary) > 0)

if __name__ == '__main__':
    unittest.main()
