# tests/test_crawler.py
import unittest
from scanner.crawler import Crawler

class TestCrawler(unittest.TestCase):
    def test_crawl(self):
        crawler = Crawler("http://example.com")
        crawler.crawl("http://example.com")
        self.assertTrue(len(crawler.visited_urls) > 0)

if __name__ == "__main__":
    unittest.main()