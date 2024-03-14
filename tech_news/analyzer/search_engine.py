from tech_news.database import db

# Requisito 7
def search_by_title(title):
    try:
        news = db.news.find(
            {"title":
             {"$regex": title, "$options": "i"}
            },
            projection=["title", "url"],
        )

        list_news = [(new["title"], new["url"]) for new in news]
        return list_news

    except Exception as error:
        raise error


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
