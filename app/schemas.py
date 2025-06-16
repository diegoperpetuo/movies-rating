from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    name: str
    password: str

class UserLogin(BaseModel):
    name: str
    password: str

class RatingCreate(BaseModel):
    title: str
    rating: float  # 0 a 10
    genre: str
    review: Optional[str] = None
