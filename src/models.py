from datetime import datetime
from pydantic import BaseModel


class Tweets(BaseModel):
    id: int
    published_at: datetime
    phrase: str
    hashtags: str
    author_id: int
    query_phrases: str
