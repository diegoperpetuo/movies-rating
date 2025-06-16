from pydantic import BaseModel
from typing import Optional

class RatingCreate(BaseModel):
    title: str
    rating: float
    genre: str
    review: Optional[str] = None