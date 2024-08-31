import unittest
from app.summarizer import generate_summary

class TestSummarizer(unittest.TestCase):
    def test_generate_summary(self):
        # Example article content
        article_content = (
            "Artificial Intelligence (AI) has become a significant part of modern technology. "
            "It is used in various applications such as voice recognition, language translation, "
            "and autonomous vehicles. The development of AI is advancing rapidly, and it has the "
            "potential to revolutionize industries and improve the quality of life."
        )
        
        # Generate summary
        summary = generate_summary(article_content)
        
        # Assert that the summary is not empty
        self.assertTrue(len(summary) > 0, "Summary should not be empty.")

if __name__ == '__main__':
    unittest.main()
