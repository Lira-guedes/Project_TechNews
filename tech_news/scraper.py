import requests
import time
from bs4 import BeautifulSoup


# Requisito 1
def fetch(url):
    try:
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"},
        )
        time.sleep(1)

        if response.status_code != 200:
            return None
        return response.text
    
    except requests.RequestException:
        return None


# Requisito 2
def scrape_updates(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    list = []

    for new in soup.find_all("article", {"class": "entry-preview"}):
        list.append(new.find("a", href=True)["href"])

    return list


# Requisito 3
def scrape_next_page_link(html_content):
    soup = BeautifulSoup(html_content, "html.parser")

    try:
        return soup.find("a", {"class": "next"}, href=True)["href"]
    except TypeError:
        return None


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
