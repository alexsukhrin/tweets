"""Serializable Model Data."""
from datetime import datetime
from pydantic import BaseModel


class Tweets(BaseModel):
    """Schema twwets."""

    id: int
    published_at: datetime
    phrase: str
    hashtags: str
    author_id: int
    query_phrases: str


class Hashtags(BaseModel):
    """Schema hashtags."""

    hashtags: str
    count_hashtags: int


class Users(BaseModel):
    """Schema users."""

    author_id: int
    count_tweets: int


class Amount(BaseModel):
    """Schema amount."""

    amount: int
