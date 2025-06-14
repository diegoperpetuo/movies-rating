from pydantic import BaseModel
from typing import Optional

class RatingCreate(BaseModel):
    title: str
    rating: float  # 0 a 10
    genre: str
    review: Optional[str] = None
