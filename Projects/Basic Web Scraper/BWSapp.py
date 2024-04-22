import tkinter as tk
from tkinter import messagebox
from BaiscWebScraper import WebScraper

class WebScraperGUI:
    def __init__(self, master):
        self.master = master
        master.title("Web Scraper")

        self.label = tk.Label(master, text="Enter URL:")
        self.label.pack()

        self.url_entry = tk.Entry(master)
        self.url_entry.pack()

        self.scrape_button = tk.Button(master, text="Scrape", command=self.scrape)
        self.scrape_button.pack()

    def scrape(self):
        url = self.url_entry.get()
        scraper = WebScraper(url)
        html_content = scraper.get_html_content()
        if html_content:
            scraper.extract_information(html_content)
        else:
            messagebox.showerror("Error", "Failed to fetch HTML content from the provided URL.")

def main():
    root = tk.Tk()
    app = WebScraperGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
