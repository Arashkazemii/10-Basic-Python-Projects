# Web Scraper

This project utilizes the Tkinter library along with the "BaiscWebScraper" module to extract information from web pages.

## Features

- Inputting the URL of a web page for information extraction.
- Using the "Scrape" button to initiate the extraction process.
- Displaying an error message if failed to fetch HTML content from the provided URL.

## Requirements

- Python 3.x
- Tkinter library
- BeautifulSoup library

## How to Use

1. Run the Python script.
2. Input the URL of the desired web page.
3. Click the "Scrape" button to start the extraction process.
4. Upon success, the extracted information will be displayed. Otherwise, an error message will be shown.

## Sample Code

```python
import tkinter as tk
from tkinter import messagebox
from bs4 import BeautifulSoup


class WebScraper:
    def __init__(self, url):
        self.url = url

    def get_html_content(self):
         # Code To Get URL

    def extract_information(self, html_content):
        # Code To Extract html


class WebScraperGUI:
    def init(self, master):
        # Code for initializing the GUI

    def scrape(self):
        # Code for scraping the webpage

def main():
    # Code for running the main application

if name == "main":
    main()
```
By following these instructions, users can easily extract the information they need from web pages.