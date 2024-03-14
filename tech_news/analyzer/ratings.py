from tech_news.database import db


# Requisito 10
def top_5_categories():
    try:
        categories = db.news.aggregate([
            {"$group": {"_id": "$category", "count": {"$sum": 1}}},
            {"$sort": {"count": -1, "_id": 1}},
            {"$limit": 5}
        ])

        categories_list = [category["_id"] for category in categories]
        return categories_list

    except Exception as error:
        raise error
