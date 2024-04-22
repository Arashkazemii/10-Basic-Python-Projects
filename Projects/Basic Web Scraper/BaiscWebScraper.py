import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, url):
        self.url = url

    def get_html_content(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.text
        else:
            print("Error: ", response.status_code)
            return None

    def extract_information(self, html_content):
        if html_content:
            soup = BeautifulSoup(html_content, 'html.parser')
            # Extracting title
            title = soup.title.text
            print("Title: ", title)
            
            # Extracting links
            links = soup.find_all('a')
            print("Links: ")
            for link in links:
                print(link.get('href'))

    def scrape(self):
        html_content = self.get_html_content()
        self.extract_information(html_content)

# Usage example
# url = 'https://example.com'
# scraper = WebScraper(url)
# scraper.scrape()
