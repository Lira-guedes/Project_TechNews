import requests
import time
from bs4 import BeautifulSoup
import re
from tech_news.database import create_news


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
    soup = BeautifulSoup(html_content, "html.parser")
    reading_time_text = soup.find("li", {"class": "meta-reading-time"}).text

    return {
        "url": soup.find("link", {"rel": "canonical"})["href"],
        "title": soup.find("h1", {"class": "entry-title"}).text.strip(),
        "timestamp": soup.find("li", {"class": "meta-date"}).text,
        "writer": soup.find("span", {"class": "author"}).a.text,
        "reading_time": int(re.search(r'\d+', reading_time_text).group()),
        "summary": soup.find("div", {"class": "entry-content"}).p.text.strip(),
        "category": soup.find("span", {"class": "label"}).text.strip(),
    }


# Requisito 5
def get_tech_news(amount):
    news = []
    URL = "https://blog.betrybe.com/"

    while len(news) < amount:
        response = fetch(URL)
        links = scrape_updates(response)

        for link in links:
            news_content = fetch(link)
            news.append(scrape_news(news_content))
            if len(news) == amount:
                break
            if len(news) < amount:
                URL = scrape_next_page_link(response)

    create_news(news)
    return news
