import requests
from bs4 import BeautifulSoup

CATEGORIES = ["national", "business", "sports", "world", "politics", "technology", "entertainment", "automobile"]

def get_headlines():
    headlines = []

    for category in CATEGORIES:
        url = f"https://inshorts.com/en/read/{category}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        for item in soup.find_all('span', itemprop='headline'):
            title = item.text.strip()
            headlines.append(title)

    return list(set(headlines))  # remove duplicates
