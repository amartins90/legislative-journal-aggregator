import os
import re
import requests

from bs4 import BeautifulSoup
from urllib.parse import urljoin

LEGISLATIVE_HOUSE_URL = 'https://imprensaoficial.jundiai.sp.gov.br/'

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0"
})

document_urls = []

response = session.get(LEGISLATIVE_HOUSE_URL)
response.raise_for_status()

journal_pattern = r'^' + re.escape(LEGISLATIVE_HOUSE_URL + "edicao-")  + r'\d+/$'

soup = BeautifulSoup(response.text, "html.parser")
for a in soup.find_all("a", href=True):
    href = a["href"]

    if re.fullmatch(journal_pattern, href):
        document_urls.append(href)


journal_pattern = r'^' + re.escape(LEGISLATIVE_HOUSE_URL + "wp-content/uploads/")  + r'.*\.pdf$'

for document_url in document_urls:

    response = session.get(document_url)
    response.raise_for_status()

    document_soup = BeautifulSoup(response.text, "html.parser")
    for a in document_soup.find_all("a", href=True):
        href = a["href"]
        if re.fullmatch(journal_pattern, href):
            print(href)