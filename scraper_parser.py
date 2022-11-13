import requests
from bs4 import BeautifulSoup

def get_page_html_parser(url):
    HEADERS = ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36', 
        'Accept-Language': 'pt-BR, en;q=0.5'})
    
    page = requests.get(url, headers=HEADERS)

    if page.status_code == 200:
        return BeautifulSoup(page.content, 'html.parser')