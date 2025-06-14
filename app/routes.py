from fastapi import APIRouter, Depends, HTTPException
from bson import ObjectId
from app.schemas import RatingCreate
from app.auth import get_current_user
from app.database import db
from app.models import rating_dict

router = APIRouter()

@router.post("/")
def create_rating(rating: RatingCreate, user_id: str = Depends(get_current_user)):
    ratings = db["ratings"]
    new_rating = rating_dict(user_id, rating)
    result = ratings.insert_one(new_rating)
    return {"message": "Rating created", "id": str(result.inserted_id)}

@router.get("/")
def get_user_ratings(user_id: str = Depends(get_current_user)):
    ratings = db["ratings"]
    user_ratings = list(ratings.find({"user_id": user_id}, {"_id": 0}))
    return user_ratings

@router.delete("/{title}")
def delete_rating(title: str, user_id: str = Depends(get_current_user)):
    ratings = db["ratings"]
    result = ratings.delete_one({"user_id": user_id, "title": title})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Rating not found")
    return {"message": "Rating deleted"}
