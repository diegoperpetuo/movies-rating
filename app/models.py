from datetime import datetime

def rating_dict(user_id: str, data):
    return {
        "user_id": user_id,
        "title": data.title,
        "rating": data.rating,
        "genre": data.genre,
        "review": data.review,
        "created_at": datetime.utcnow()
    }
