"""The main file to start the service."""
from fastapi import FastAPI
import uvicorn
import asyncpg
from typing import List

from models import Tweets, Amount, Users, Hashtags
import config
from handler import ApiHandler

app = FastAPI()


@app.on_event("startup")
async def startup():
    """Create pool connect to db."""
    app.loop = await asyncpg.create_pool(
        user=config.POSTGRES_USER,
        password=config.POSTGRES_PASSWORD,
        host=config.POSTGRES_HOST,
        port=config.POSTGRES_PORT,
    )


@app.on_event("shutdown")
async def shutdown():
    """Close pool connect db."""
    await app.pool.close()


@app.get("/", response_model=List[Tweets])
async def tweets(offset: int = 0, limit: int = 100) -> list:
    """Get tweets."""
    return await ApiHandler(pool=app.pool).tweets(limit=limit, offset=offset)


@app.get("/amount", response_model=List[Amount])
async def amount() -> list:
    """Get amount for tweets."""
    return await ApiHandler(pool=app.pool).amount()


@app.get("/hashtags", response_model=List[Hashtags])
async def hashtags(limit: int = 3) -> list:
    """Get top three hashtags."""
    return await ApiHandler(pool=app.loop).hashtags(limit=limit)


@app.get("/users", response_model=List[Users])
async def users(limit: int = 3) -> list:
    """Get top three users."""
    return await ApiHandler(pool=app.loop).users(limit=limit)


if __name__ == '__main__':
    uvicorn.run(app, host=config.HOST, port=int(config.PORT))
