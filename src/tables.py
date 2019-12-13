from sqlalchemy import (
    MetaData,
    Table,
    Column,
    Integer,
    DateTime,
    Text,
    create_engine
)
from config import DATABASE_URL

metadata = MetaData()

tweets = Table(
    "tweets", metadata,
    Column("id", Integer, primary_key=True),
    Column("published_at", DateTime),
    Column("phrase", Text),
    Column("hashtags", Text),
    Column("author_id", Integer),
    Column("query_phrases", Text),
)

engine = create_engine(DATABASE_URL)
metadata.create_all(engine)
