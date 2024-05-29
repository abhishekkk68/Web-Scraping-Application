from flask import Flask, render_template, request, redirect, url_for, send_file
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from urllib.parse import urljoin

app = Flask(__name__)

class WebScraper:
    def __init__(self, base_url, user_agent='Mozilla/5.0'):
        self.base_url = base_url
        self.headers = {'User-Agent': user_agent}
        self.data = []

    def get_soup(self, url):
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return BeautifulSoup(response.content, 'html.parser')
        else:
            print(f'Failed to retrieve the webpage. Status code: {response.status_code}')
            return None

    def scrape_page(self, soup):
        title = soup.find('title').get_text() if soup.find('title') else 'No Title'
        headings = [heading.get_text() for heading in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])]
        paragraphs = [p.get_text() for p in soup.find_all('p')]
        images = [img['src'] for img in soup.find_all('img') if 'src' in img.attrs]
        links = [a['href'] for a in soup.find_all('a') if 'href' in a.attrs]

        self.data.append({
            'title': title,
            'headings': '\n'.join(headings),
            'paragraphs': '\n'.join(paragraphs),
            'images': '\n'.join(images),
            'links': '\n'.join(links)
        })

    def scrape(self, start_url):
        next_url = start_url
        while next_url:
            print(f'Scraping {next_url}')
            soup = self.get_soup(next_url)
            if soup:
                self.scrape_page(soup)
                next_url = self.get_next_page(soup)
                time.sleep(1)  # Be polite by waiting a bit before making the next request
            else:
                break

    def get_next_page(self, soup):
        next_page_tag = soup.find('a', text='Next')
        if next_page_tag:
            return urljoin(self.base_url, next_page_tag['href'])
        else:
            return None

    def save_to_excel(self, file_name):
        df = pd.DataFrame(self.data)
        df.to_excel(file_name, index=False)
        print(f'Data saved to {file_name}')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form['url']
    if url:
        scraper = WebScraper(base_url=url)
        scraper.scrape(url)
        file_name = 'scraped_data.xlsx'
        scraper.save_to_excel(file_name)
        return send_file(file_name, as_attachment=True)
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
