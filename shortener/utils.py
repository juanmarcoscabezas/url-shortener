import hashlib
import base64
import requests
from bs4 import BeautifulSoup

def shorten_url(url):
    url_bytes = url.encode('utf-8')
    hash_bytes = hashlib.sha256(url_bytes).digest()

    short_bytes = hash_bytes[:8]
    short_url = base64.b64encode(short_bytes).decode('utf-8')

    return short_url

def get_page_title(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('title')
        return title.get_text()
    except:
        return None