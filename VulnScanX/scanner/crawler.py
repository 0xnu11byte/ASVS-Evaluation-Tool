# scanner/crawler.py
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class Crawler:
    def __init__(self, base_url, max_depth=2):
        """
        Initialize the Crawler with a base URL and maximum crawling depth.
        """
        self.base_url = base_url
        self.max_depth = max_depth
        self.visited_urls = set()

    def crawl(self, url, depth=0):
        """
        Recursively crawl the website up to the specified depth.
        """
        if depth > self.max_depth or url in self.visited_urls:
            return
        self.visited_urls.add(url)
        print(f"Crawling: {url} (Depth: {depth})")

        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            for link in soup.find_all('a', href=True):
                full_url = urljoin(self.base_url, link['href'])
                if self.base_url in full_url:
                    self.crawl(full_url, depth + 1)
        except requests.RequestException as e:
            print(f"Error crawling {url}: {e}")

    def get_visited_urls(self):
        """
        Return the list of visited URLs.
        """
        return list(self.visited_urls)