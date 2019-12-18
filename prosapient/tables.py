from sqlalchemy import (  # type: ignore
    MetaData,
    Table,
    Column,
    Integer,
    DateTime,
    Text,
    create_engine,
    BIGINT,
)

try:
    from .config import DATABASE_URL
except ImportError:
    # if the package path was not found in Docker
    from config import DATABASE_URL

metadata = MetaData()

tweets = Table(
    "tweets", metadata,
    Column("id", Integer, primary_key=True),
    Column("tweet_id", BIGINT, unique=True),
    Column("published_at", DateTime),
    Column("phrase", Text),
    Column("hashtags", Text),
    Column("author_id", BIGINT),
    Column("query_phrases", Text),
)

engine = create_engine(DATABASE_URL)
metadata.create_all(engine)
