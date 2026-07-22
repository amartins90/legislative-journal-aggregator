import os
import re
import requests

from bs4 import BeautifulSoup
from urllib.parse import urljoin

# TODO add logging
# TODO add pydantic

class Scraper:

    def __init__(self, house_url):
        self.house_url = house_url
        return

    def get_latest_editions(self):
        session = requests.Session()
        session.headers.update({
            "User-Agent": "Mozilla/5.0"
        })
        response = session.get(self.house_url)
        response.raise_for_status()

        document_urls = []
        journal_pattern = r'^' + re.escape(self.house_url + "edicao-")  + r'\d+/$'
        soup = BeautifulSoup(response.text, "html.parser")
        for a in soup.find_all("a", href=True):
            if re.fullmatch(journal_pattern, a["href"]):
                document_urls.append(a["href"])

        return document_urls

    def persist_files(self):
        return

# journal_pattern = r'^' + re.escape(LEGISLATIVE_HOUSE_URL + "wp-content/uploads/")  + r'.*\.pdf$'

# for document_url in document_urls:

#     response = session.get(document_url)
#     response.raise_for_status()

#     document_soup = BeautifulSoup(response.text, "html.parser")
#     for a in document_soup.find_all("a", href=True):
#         href = a["href"]
#         if re.fullmatch(journal_pattern, href):
#             print(href)