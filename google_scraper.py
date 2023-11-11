import requests
import re
from bs4 import BeautifulSoup

URL_SEARCH = "https://www.google.com/search?client=firefox-b-d&q=intext:\"@DOMAIN\""
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0"
}
EMAIL_PATTERN = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"


def _make_request(domain):
    url = URL_SEARCH.replace("DOMAIN", domain)
    r = requests.get(url, headers=HEADERS)
    
    if r.status_code == 200:
        return r.text
    else:
        print(f"Error: {r.status_code} on www.google.com")

def extract_mails(domain):
    html = _make_request(domain)
    if not html:
        return

    soup = BeautifulSoup(html, 'html.parser')
    descriptions = soup.findAll(class_ = "VwiC3b yXK7lf lyLwlc yDYNvb W8l4ac lEBKkf")

    emails_list = []
    for description in descriptions:
        emails = re.findall(EMAIL_PATTERN, description.text)
        if len(emails) > 0:
            for email in emails:
                if not "info" in email and not "hello" in email and not "hola" in email and domain in email:
                    emails_list.append(email)

    return emails_list