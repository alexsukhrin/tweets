from datetime import datetime
from pydantic import BaseModel


class Tweets(BaseModel):
    id: int
    published_at: datetime
    phrase: str
    hashtags: str
    author_id: int
    query_phrases: str


class Hashtags(BaseModel):
    hashtags: str
    count_hashtags: int


class Users(BaseModel):
    author_id: int
    count_tweets: int


class Amount(BaseModel):
    amount: int
